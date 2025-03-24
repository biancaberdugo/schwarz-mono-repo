import uvicorn
from fastapi import FastAPI

from src.api.dependencies.containers import (
    get_config,
    ServiceContainer,
    ExternalDependenciesContainer,
)
from src.api.openapi import setup_openapi_routers

app_config = get_config()
app = FastAPI(title=app_config.service, version=app_config.version)

app.services_deps = ServiceContainer()
app.services_deps.wire(
    packages=[
        "src.api.endpoints",
    ]
)

setup_openapi_routers(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
