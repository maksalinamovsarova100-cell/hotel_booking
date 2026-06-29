from datetime import UTC, datetime

import jwt

from app.core.config import settings
from app.auth.constants import (
    ACCESS_TOKEN_EXPIRE,
    ALGORITHM,
)


def create_access_token(data: dict) -> str:
    payload = data.copy()

    payload["exp"] = datetime.now(UTC) + ACCESS_TOKEN_EXPIRE

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )