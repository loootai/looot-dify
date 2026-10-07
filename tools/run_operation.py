import json
import uuid
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import LoootError, call


class RunOperationTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        raw_input = tool_parameters.get("input") or "{}"
        try:
            parsed = json.loads(raw_input) if isinstance(raw_input, str) else raw_input
        except ValueError as exc:
            raise ValueError(f"input must be valid JSON: {exc}") from exc
        if not isinstance(parsed, dict):
            raise ValueError("input must be a JSON object")
        body: dict[str, Any] = {
            "endpointId": tool_parameters.get("endpoint_id", ""),
            "input": parsed,
            "idempotencyKey": (tool_parameters.get("idempotency_key") or "").strip() or f"dify-{uuid.uuid4()}",
            "wait": int(tool_parameters.get("wait") if tool_parameters.get("wait") is not None else 20),
        }
        if tool_parameters.get("fallback", True):
            max_cost = float(tool_parameters.get("max_cost_usd") or 0)
            body["fallback"] = {"enabled": True, "maxCostUsd": max_cost} if max_cost > 0 else True
        try:
            yield self.create_json_message(call(self.runtime.credentials["api_key"], "POST", "/v1/runs", body=body))
        except LoootError as exc:
            raise ValueError(str(exc)) from exc
