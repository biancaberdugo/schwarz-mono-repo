from typing import Optional, Dict, Any

from requests import Response
from starlette.testclient import TestClient

from src.api.models.dto.v1.trips import TripRequestV1


def _post(
    client: TestClient,
    endpoint: str,
    payload: Optional[dict] = None,
    headers: Dict[str, Any] = None,
    params: Dict[str, Any] = None,
) -> Response:
    params = {} if params is None else params
    headers = {} if headers is None else headers

    return client.post(endpoint, json=payload, headers=headers, params=params)


def post_send_simulate_metrics_taxi_coordinates(client: TestClient):
    return _post(
        client=client,
        endpoint="/api/v1/simulate-events/taxi-route/trip-coordinates/",
    )


def post_simulate_new_trip_request(client: TestClient, payload: TripRequestV1):
    return _post(
        client=client, endpoint="/api/v1/trips/new/", payload=payload.model_dump()
    )
