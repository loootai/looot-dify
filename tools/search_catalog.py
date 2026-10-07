from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import LoootError, call


class SearchCatalogTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        params: dict[str, Any] = {
            "q": tool_parameters.get("query", ""),
            "limit": int(tool_parameters.get("limit") or 10),
        }
        for key in ("provider", "category", "prefer"):
            value = tool_parameters.get(key)
            if value:
                params[key] = value
        try:
            yield self.create_json_message(call(self.runtime.credentials["api_key"], "GET", "/v1/catalog/search", params=params))
        except LoootError as exc:
            raise ValueError(str(exc)) from exc
