from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from characters import CHARACTERS
from services.providers import groq_provider,openrouter_provider

router = APIRouter()



@router.get("/",tags=["personas"],name="Get all Personas")
async def read_users():
    return [{name: character.to_dict() for name,character in CHARACTERS.items()}]


@router.post("/chat")
async def chat(payload: dict):

    character = CHARACTERS[
        payload["character"]
    ]

    stream = groq_provider.generate_response(
        character=character,
        message=payload["message"]
    )

    return StreamingResponse(
        stream,
        media_type="text/event-stream"
    )