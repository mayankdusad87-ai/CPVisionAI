"""
=========================================================
ChannelIQ AI

Groq Provider

Concrete implementation of the AIProvider interface.

Responsibilities
----------------
1. Connect to Groq
2. Send prompts
3. Parse JSON
4. Retry on transient failures
5. Return Python dictionary

=========================================================
"""

from __future__ import annotations

import json
import logging
import time
from typing import Any

import streamlit as st
from groq import Groq

from core.ai.provider import AIProvider

logger = logging.getLogger(__name__)


class GroqProvider(AIProvider):
    """
    Groq implementation.

    Used by Consulting Engine.
    """

    def __init__(self):

        api_key = st.secrets.get("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found in Streamlit Secrets."
            )

        self._client = Groq(api_key=api_key)

        self._model = st.secrets.get(
            "GROQ_MODEL",
            "llama-3.3-70b-versatile",
        )

    # =====================================================
    # PROPERTIES
    # =====================================================

    @property
    def provider_name(self) -> str:

        return "Groq"

    @property
    def model_name(self) -> str:

        return self._model

    # =====================================================
    # HEALTH CHECK
    # =====================================================

    def health_check(self) -> bool:

        try:

            self._client.models.list()

            return True

        except Exception as ex:

            logger.exception(ex)

            return False

    # =====================================================
    # GENERATE
    # =====================================================

    def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        max_output_tokens: int = 3000,
    ) -> dict[str, Any]:

        retries = 3

        for attempt in range(retries):

            try:

                response = self._client.chat.completions.create(

                    model=self._model,

                    temperature=temperature,

                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt,
                        },
                        {
                            "role": "user",
                            "content": user_prompt,
                        },
                    ],
                )

                text = (
                    response
                    .choices[0]
                    .message
                    .content
                    .strip()
                )

                if text.startswith("```json"):

                    text = (
                        text.replace("```json", "")
                        .replace("```", "")
                        .strip()
                    )

                return json.loads(text)

            except json.JSONDecodeError:

                logger.exception(
                    "Invalid JSON returned by AI."
                )

                raise ValueError(
                    "AI response is not valid JSON."
                )

            except Exception as ex:

                logger.warning(
                    f"Attempt {attempt+1} failed: {ex}"
                )

                if attempt == retries - 1:
                    raise

                time.sleep(2)

        raise RuntimeError(
            "Groq generation failed."
        )
