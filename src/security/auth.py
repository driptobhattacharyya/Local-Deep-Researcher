import os
from typing import Any, Dict

from langchain_core.runnables import RunnableConfig


async def auth(config: RunnableConfig) -> Dict[str, Any]:
    """Auth hook for LangGraph Studio/Server sessions.

    Returns metadata for the current session (e.g., user/owner id). If an auth
    token is provided via environment variable or config, you can validate it
    here and attach the user identity. For local usage, we default to a single
    local user.
    """
    owner = os.getenv("LG_OWNER") or config.get("metadata", {}).get("owner") or "local-user"
    # You can extend this to validate tokens from headers/config and map to user ids
    return {"owner": owner}
