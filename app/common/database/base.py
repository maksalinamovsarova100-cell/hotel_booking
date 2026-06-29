from sqlalchemy.orm import DeclarativeBase

from .mixins import TimestampMixin
from .mixins import UUIDMixin


class Base(
    DeclarativeBase,
    UUIDMixin,
    TimestampMixin,
):
    pass