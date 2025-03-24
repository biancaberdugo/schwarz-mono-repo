from types import ModuleType
from typing import Dict, cast, Optional, Tuple

from fastapi import FastAPI, APIRouter
from starlette.responses import RedirectResponse

from src.api.endpoints import (
    RouterInfo,
    router_versions,
    events_simulation,
    trips_simulation,
)

app_router = APIRouter()


@app_router.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


def _include_router(
    app: FastAPI, module: ModuleType, router_info: RouterInfo, version: int
) -> Optional[Tuple[str, RouterInfo]]:
    """
        Searches on the loaded module the object router_vX aiming to include on FastAPI app the routes
    :param app: FastAPI app
    :param module: module under endpoints folder
    :param router_info: RouterInfo defined on an endpoint class, containing the route name and description
    :param version: specify the route version forcing the endpoint versioning prefix
    :return: dict containing the route name and the created TracingAPIRouter
    """

    router_attr_name = f"router_v{version}"
    version_router = getattr(
        module, router_attr_name, None
    )  # gets the router_vX object from the loaded module

    if not version_router:
        return None

    name_suffix = f" v{version}"
    name = router_info.name + name_suffix
    app.include_router(version_router, tags=[name])
    return name, router_info


def _include_all_routers(app: FastAPI, module: ModuleType) -> Dict[str, RouterInfo]:
    """
        For a given module, register all version routes
    :param app: FastAPI app
    :param module: module under endpoints folder
    :return: dict with routes names and RouterInfo
    """
    routers_info = {}
    router_info = cast(
        RouterInfo, getattr(module, "router_info")
    )  # get defined router information into a dict

    # Specific version routers.
    for version in router_versions():
        result = _include_router(app, module, router_info, version)
        if result is not None:
            routers_info[result[0]] = result[1]

    return routers_info


def setup_routing(app: FastAPI) -> Dict[str, RouterInfo]:
    """
        Get all routes defined into a class and register it in a FastAPI application.

    :param app: FastAPI app
    :param module: module under endpoints folder

    """
    routers_info = {}

    routers_info.update(_include_all_routers(app, events_simulation))
    routers_info.update(_include_all_routers(app, trips_simulation))

    app.include_router(app_router, include_in_schema=False)

    return routers_info
