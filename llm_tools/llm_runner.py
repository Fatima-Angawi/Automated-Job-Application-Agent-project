"""Lightweight LLM runner abstraction (stub)."""
from typing import Any

class LLMRunner:
    def __init__(self, client=None):
        self.client = client

    def run(self, prompt: str, **kwargs) -> str:
        """Run the prompt through the configured LLM. Return text response.

        This is a stub — wire to LangChain / OpenAI / other provider later.
        """
        # For now return a placeholder
        return "[LLM response placeholder]"
