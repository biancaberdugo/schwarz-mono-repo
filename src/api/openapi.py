from copy import deepcopy
from typing import Dict, Any

from fastapi import FastAPI

from src.api.routing import setup_routing


def _get_current_openapi_schema(app: FastAPI) -> Dict[str, Any]:
    return deepcopy(app.openapi())


def setup_openapi_routers(app: FastAPI):
    """
    See https://fastapi.tiangolo.com/tutorial/metadata/#use-your-tags
    """
    routers_info = setup_routing(app)

    openapi_schema = _get_current_openapi_schema(app)
    tags_metadata = [
        {"name": k, **v.to_tags_metadata()} for k, v in routers_info.items()
    ]
    tags = openapi_schema.get("tags", [])
    tags.extend(tags_metadata)
    openapi_schema["tags"] = tags
    app.openapi_schema = openapi_schema
