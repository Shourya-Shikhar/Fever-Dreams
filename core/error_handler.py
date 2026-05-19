from fastapi import HTTPException
import traceback

from openai import (
    RateLimitError,
    AuthenticationError,
    APIConnectionError,
    InternalServerError,
)


def handle_provider_error(character, error):
    print(traceback.format_exc())
    error_map = {
        RateLimitError: (
            429,
            "rate_limit"
        ),
        AuthenticationError: (
            401,
            "auth"
        ),
        APIConnectionError: (
            503,
            "connection"
        ),
        InternalServerError: (
            500,
            "internal"
        ),
    }

    for error_type, (
        status_code,
        error_key
    ) in error_map.items():
        if isinstance(error, error_type):
            raise HTTPException(
                status_code=status_code,
                detail=character.error_responses.get(
                    error_key,
                    character.error_responses["unknown"]
                )
            )
    raise HTTPException(
        status_code=500,
        detail={character.name:character.error_responses["unknown"],"error":str(error)}
    )