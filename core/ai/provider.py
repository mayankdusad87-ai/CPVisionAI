"""
=========================================================
ChannelIQ AI

AI Provider

Abstract interface for all AI providers.

Every AI provider (OpenAI, Gemini,
Claude, OpenRouter etc.) must inherit
from this class.

=========================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class AIProvider(ABC):
    """
    Base interface for every AI provider.

    The Consulting Engine should ONLY
    communicate with this interface.

    Never directly call OpenAI or Gemini
    outside the provider implementation.
    """

    def __init__(self):

        super().__init__()

    # =====================================================
    # GENERATE
    # =====================================================

    @abstractmethod
    def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        max_output_tokens: int = 3000,
    ) -> dict[str, Any]:
        """
        Generate a structured JSON response.

        Parameters
        ----------
        system_prompt
            AI behaviour.

        user_prompt
            Business context + findings.

        temperature
            Creativity level.

        max_output_tokens
            Maximum tokens.

        Returns
        -------
        dict

            Parsed JSON response.

        Raises
        ------
        Exception

            Provider specific exception.
        """

        raise NotImplementedError

    # =====================================================
    # HEALTH CHECK
    # =====================================================

    @abstractmethod
    def health_check(
        self,
    ) -> bool:
        """
        Returns True if provider
        is reachable.

        Used during application startup.
        """

        raise NotImplementedError

    # =====================================================
    # PROVIDER NAME
    # =====================================================

    @property
    @abstractmethod
    def provider_name(
        self,
    ) -> str:
        """
        Example

        OpenAI

        Gemini

        Claude

        OpenRouter
        """

        raise NotImplementedError

    # =====================================================
    # MODEL NAME
    # =====================================================

    @property
    @abstractmethod
    def model_name(
        self,
    ) -> str:
        """
        Returns currently configured model.
        """

        raise NotImplementedError
