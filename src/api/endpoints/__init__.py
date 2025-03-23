import inspect
from functools import wraps
from typing import Set, Callable, Any, Optional, Dict

from fastapi import APIRouter
from pydantic import BaseModel, Field

__VERSIONS: Set[int] = set()


class TracingAPIRouter(APIRouter):

    def add_api_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        """
            Add the endpoint to FastApi APIRouter
        :param path: the route path
        :param endpoint: the method that will be executed when reaching the path endpoint
        :param kwargs: general kwargs requested when using the endpoint
        :return: None
        """
        super().add_api_route(path, endpoint, **kwargs)


def create_router_for_version(version: int, **kwargs) -> APIRouter:
    __VERSIONS.add(version)
    version_prefix = f"/api/v{version}"
    return TracingAPIRouter(prefix=version_prefix, **kwargs)


def router_versions() -> Set[int]:
    return __VERSIONS.copy()


class RouterInfo(BaseModel):
    name: str = Field(min_length=1)
    description: Optional[str] = None

    def to_tags_metadata(self) -> Dict[str, Any]:
        metadata = {}
        if self.description:
            metadata["description"] = self.description
        return metadata
