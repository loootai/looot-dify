from collections.abc import Generator
from typing import Any
from urllib.parse import quote

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import LoootError, call


class GetRunTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        run_id = quote(str(tool_parameters.get("run_id", "")), safe="")
        try:
            yield self.create_json_message(call(self.runtime.credentials["api_key"], "GET", f"/v1/runs/{run_id}"))
        except LoootError as exc:
            raise ValueError(str(exc)) from exc
