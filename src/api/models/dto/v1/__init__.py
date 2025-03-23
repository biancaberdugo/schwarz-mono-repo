from abc import ABC
from typing import Dict, Generic, Optional, TypeVar

from pydantic import Field, BaseModel


class DataResponseV1(BaseModel, ABC):
    """Data responses must be objects (effectively wrapper) as opposed to arrays or single object.
    That gives more flexibility to evolve the responses without breaking the clients.

    See https://docs.google.com/document/d/1ldRn2eD1Ef8L6A7mR9e69_YjlUWVaAAXnvBzBq9KjMg/edit#heading=h.kqi2ffw32frd
    """

    pass


class PaginationResponseV1(BaseModel, ABC):
    """MesHub should, for the most part, standardise on the pagination strategy by given different endpoints
    may have different needs or even different backing stores, we might need to accommodate multiple strategies.

    See https://docs.google.com/document/d/1ldRn2eD1Ef8L6A7mR9e69_YjlUWVaAAXnvBzBq9KjMg/edit#heading=h.1fvoftqw6w3y
    """

    pass


class NoopPaginationResponseV1(PaginationResponseV1):
    pass


class OffsetPaginationResponseV1(PaginationResponseV1):
    limit: int
    page: int
    total: Optional[int] = None


class CursorPaginationResponseV1(PaginationResponseV1):
    limit: int
    next_page_token: Optional[str] = None  # None when there are no items left.


DATA = TypeVar("DATA", bound=DataResponseV1)
PAGINATION = TypeVar("PAGINATION", bound=PaginationResponseV1)


class EndpointSuccessResponseV1(BaseModel, Generic[DATA, PAGINATION]):
    data: DATA
    pagination: Optional[PAGINATION] = None
    metadata: Dict[str, str] = Field(default_factory=dict)


class EndpointErrorResponseV1(BaseModel):
    data: DATA
