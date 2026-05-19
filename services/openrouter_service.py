import os
from openai import OpenAI
from dotenv import load_dotenv

from core.error_handler import handle_provider_error
from services.ai_provider import AIProvider


load_dotenv()


class OpenRouterProvider(AIProvider):
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )

    def generate_response(
        self,
        character,
        message: str
    ):
            try:
                completion = self.client.chat.completions.create(
                    model="meta-llama/llama-3.1-8b-instruct:free",
                    messages=[
                        {
                            "role": "system",
                            "content": character.build_system_prompt()
                        },
                        {
                            "role": "user",
                            "content": message
                        }
                    ],
                    stream=True,
                    temperature=1.2,
                    top_p=0.6,
                    max_tokens=200,
                )

                for chunk in completion:
                    if not chunk.choices:
                        continue
                    delta = chunk.choices[0].delta.content
                    if delta:
                        yield f"data: {delta}\n\n"

                yield "data: [DONE]\n\n"
                
            except Exception as e:
                handle_provider_error(
                        character,
                        e
                    )
            