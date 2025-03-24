from pydantic import BaseModel

from src.api.models.dto.v1.trips import TripRequestV1, TripResponseV1


class TripRequest(BaseModel):
    event_id: str
    user_id: str
    longitude_start: float
    longitude_end: float
    latitude_start: float
    latitude_end: float

    @classmethod
    def from_bff_dto_v1(cls, trip_request: TripRequestV1) -> "TripRequest":
        """
            In case of changes between DTOs the internal object can deal with multiple versions without affecting service layer
            Creates an internal object based on DTO v1
        :param trip_request:
        :return:
        """
        return cls(
            event_id=trip_request.event_id,
            user_id=trip_request.user_id,
            longitude_start=trip_request.longitude_start,
            longitude_end=trip_request.longitude_end,
            latitude_start=trip_request.latitude_start,
            latitude_end=trip_request.latitude_end,
        )

    def to_external_service_dto(self):
        # Imagine that here we are doing any necessary transformation to send this request to the expected
        # DTO requested by the external trips service
        # for testing proposes just returning the same object
        return self


class TripResponse(BaseModel):
    event_id: str
    user_id: str
    driver_id: str

    @classmethod
    def from_external_service_dto(cls, response: dict) -> "TripResponse":
        return cls(
            event_id=response.get("eventId"),
            user_id=response.get("userId"),
            driver_id=response.get("driverId"),
        )

    def to_bff_dto_v1(self) -> TripResponseV1:
        return TripResponseV1(
            event_id=self.event_id, user_id=self.user_id, driver_id=self.driver_id
        )
