from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import LoootError, call


class GetBalanceTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        try:
            yield self.create_json_message(call(self.runtime.credentials["api_key"], "GET", "/v1/balance"))
        except LoootError as exc:
            raise ValueError(str(exc)) from exc
