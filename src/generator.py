import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class Generator:

    def __init__(self):

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model_name = (
            "gemini-2.5-flash"
        )

    def build_prompt(
        self,
        query,
        context
    ):

        return f"""
You are a helpful research assistant.

Use ONLY the provided context.

Rules:
- Do not use outside knowledge.
- Do not make up facts.
- If the answer is not found in the context, say:
  "I could not find that information in the document."
- Keep answers concise and factual.
- Cite page numbers when available.

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    def generate(
        self,
        query,
        context
    ):

        prompt = self.build_prompt(
            query,
            context
        )

        try:

            response = (
                self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt
                )
            )

            return response.text

        except Exception as e:

            return (
                f"Generation Error: {str(e)}"
            )