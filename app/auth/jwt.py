from datetime import UTC, datetime, timedelta

import jwt

from app.core.config import settings


ALGORITHM = "HS256"


def create_access_token(
    user_id: int,
    email: str,
    role: str,
) -> str:

    payload = {
        "sub": str(user_id),
        "email": email,
        "role": role,
        "exp": datetime.now(UTC)
        + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )

def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[ALGORITHM],
    )