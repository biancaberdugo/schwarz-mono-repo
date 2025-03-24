import pytest
from starlette.testclient import TestClient


@pytest.fixture(scope="session", name="app")
def source_app():
    from src.api.main import app

    return app


@pytest.fixture(scope="session", name="app_client")
def get_app_client(app) -> TestClient:
    return TestClient(app)
