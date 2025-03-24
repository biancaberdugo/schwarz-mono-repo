import logging

from src.api.models.internal.trips import TripRequest, TripResponse

logger = logging.getLogger(__name__)


class TripsService:

    def request_trip(self, trip_request: TripRequest) -> TripResponse:
        """
            Entrypoint to communicates with the external Trips service
        :param trip_request: internal object that represents a trip
        :return:
        """
        logger.debug(f"Receive a trip request {trip_request.event_id}")
        # place here any extra logic that needs to be done before the call to the external Trip service
        logger.debug(f"Send the request to external service {trip_request.event_id}")
        # TODO do whatever to call the real service

        logger.debug(f"Received the external response for trip {trip_request.event_id}")

        return TripResponse.from_external_service_dto(
            response={
                "eventId": "fake_UUID",
                "userId": "fake_user_id",
                "driverId": "fake_driver_id",
            }
        )
