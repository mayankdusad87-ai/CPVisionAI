"""
=========================================================
ChannelIQ AI

OpenAI Client

Responsible ONLY for communicating with OpenAI.

No business logic.
No prompt construction.
No response parsing.

=========================================================
"""

from __future__ import annotations

import json
import logging

import streamlit as st
from openai import OpenAI


logger = logging.getLogger(__name__)


class OpenAIClient:
    """
    Wrapper around the OpenAI API.
    """

    def __init__(self):

        api_key = st.secrets.get("OPENAI_API_KEY")

        if not api_key:

            raise ValueError(
                "OPENAI_API_KEY not found in Streamlit Secrets."
            )

        self.client = OpenAI(
            api_key=api_key,
        )

        # -------------------------------------------------
        # Model
        # -------------------------------------------------

        self.model = st.secrets.get(
            "OPENAI_MODEL",
            "gpt-5",
        )

    # =====================================================
    # PUBLIC
    # =====================================================

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
    ) -> dict:

        """
        Returns parsed JSON.
        """

        try:

            response = self.client.responses.create(

                model=self.model,

                input=[

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

            text = response.output_text

            return json.loads(text)

        except json.JSONDecodeError:

            logger.exception(
                "Invalid JSON received from OpenAI."
            )

            raise ValueError(
                "AI returned invalid JSON."
            )

        except Exception as ex:

            logger.exception(ex)

            raise
