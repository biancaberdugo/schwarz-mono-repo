import pytest

from src.api.dependencies.containers import ServiceContainer


@pytest.fixture(name="container_service")
def get_services():
    container = ServiceContainer()
    return container


@pytest.fixture(name="taxi_route_service")
def get_taxi_service(container_service: ServiceContainer):
    return container_service.taxi_route_service()
