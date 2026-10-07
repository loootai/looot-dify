"""Small HTTP client for the looot REST API (https://api.looot.ai)."""

import json
from typing import Any

import requests

BASE_URL = "https://api.looot.ai"
TIMEOUT_SECONDS = 60


class LoootError(Exception):
    """Raised when the looot API answers with an error."""


def call(
    api_key: str,
    method: str,
    path: str,
    params: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Send one request to the looot API and return the parsed JSON body."""
    if not api_key:
        raise LoootError("Missing looot agent token. Add it in the plugin credentials.")
    try:
        response = requests.request(
            method,
            f"{BASE_URL}{path}",
            params=params,
            json=body,
            headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
            timeout=TIMEOUT_SECONDS,
        )
    except requests.RequestException as exc:
        raise LoootError(f"Could not reach api.looot.ai: {type(exc).__name__}") from exc
    try:
        payload = response.json()
    except ValueError:
        payload = {"raw": response.text[:500]}
    if response.status_code >= 400:
        error = payload.get("error") if isinstance(payload, dict) else None
        message = error.get("message") if isinstance(error, dict) else None
        code = error.get("code") if isinstance(error, dict) else None
        raise LoootError(f"looot returned {response.status_code} {code or ''}: {message or json.dumps(payload)[:300]}".strip())
    return payload if isinstance(payload, dict) else {"data": payload}
