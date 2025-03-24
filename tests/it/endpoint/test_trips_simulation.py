from src.api.models.dto.v1.trips import (
    TripResponseSingleEndpointSuccessResponseV1,
    TripRequestV1,
    TripResponseV1,
    TripResponseSingleDataV1,
)
from tests.it.helpers import post_simulate_new_trip_request


def test_new_trip_v1(app_client):
    result = post_simulate_new_trip_request(
        client=app_client,
        payload=TripRequestV1(
            event_id="fe3c7792-a6a2-4894-b045-5bbb3c7ddaac",
            user_id="bf2a37ab-1ef8-4e1b-9614-e44332b01ef6",
            longitude_start=-122.419416,
            longitude_end=-122.271111,
            latitude_start=37.774929,
            latitude_end=37.804363,
        ),
    )

    assert result.status_code == 200

    # Validate if the response have the expected result
    data = TripResponseSingleEndpointSuccessResponseV1.model_validate(result.json())

    assert data == TripResponseSingleEndpointSuccessResponseV1(
        data=TripResponseSingleDataV1(
            event=TripResponseV1(
                event_id="fake_UUID", user_id="fake_user_id", driver_id="fake_driver_id"
            )
        ),
        pagination=None,
        metadata={},
    )
