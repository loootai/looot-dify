from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from tools.client import LoootError, call


class LoootProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            call(credentials.get("api_key", ""), "GET", "/v1/balance")
        except LoootError as exc:
            raise ToolProviderCredentialValidationError(str(exc)) from exc
