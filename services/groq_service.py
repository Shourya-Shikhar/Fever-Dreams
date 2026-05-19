import os

from groq import Groq
from dotenv import load_dotenv

from services.ai_provider import AIProvider


load_dotenv()


class GroqProvider(AIProvider):

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )


    def generate_response(
        self,
        character,
        message: str
    ):

        try:

            completion = self.client.chat.completions.create(

                model="llama-3.1-8b-instant",

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

                temperature=0.9,
                top_p=0.8,

                max_tokens=120,
            )

            for chunk in completion:

                if not chunk.choices:
                    continue

                delta = chunk.choices[0].delta.content

                if not delta:
                    continue

                yield f"data: {delta}\n\n"

            yield "data: [DONE]\n\n"

        except Exception as e:

            print(e)

            yield (
                f"data: "
                f"{character.error_responses['unknown']}\n\n"
            )

            yield "data: [DONE]\n\n"