from discord import Embed, utils
from typing import Optional
from configurations.config import (
    MAIN_COLOR,
    SUCCESS_COLOR,
    ERROR_COLOR,
    BotData,
    FOOTER_TEXT,
)


class MainEmbed(Embed):
    """Represents a main embed with a title, description, and other properties."""

    def __init__(self, description: Optional[str] = None, title: Optional[str] = None):
        """
        Parameters
        ----------
        description: :class:`str`
            The description of the main embed.
        title: :class:`str`, default `None`
            The title of the main embed.
        """

        super().__init__(
            title=title,
            description=description,
            color=MAIN_COLOR,
            timestamp=utils.utcnow(),
        )
        self.set_footer(
            text=FOOTER_TEXT,
            icon_url=BotData.AVATAR_URL,
        )


class SuccessEmbed(Embed):
    """Represents a success embed."""

    def __init__(self, description: Optional[str] = None, title: Optional[str] = None):
        """
        Parameters
        ----------
        description: :class:`str`
            The description of the success embed.
        title: :class:`str`, default `None`
            The title of the success embed.
        """

        if title:
            title = f"<:green_check:1227876834105102397> {title}"
        super().__init__(
            title=title,
            description=description,
            color=SUCCESS_COLOR,
            timestamp=utils.utcnow(),
        )
        self.set_footer(
            text=FOOTER_TEXT,
            icon_url=BotData.AVATAR_URL,
        )


class ErrorEmbed(Embed):
    """Represents an error embed."""

    def __init__(self, description: Optional[str] = None, title: Optional[str] = None):
        """
        Parameters
        ----------
        description: :class:`str`
            The description of the error embed.
        title: :class:`str`, default `None`
            The title of the error embed.
        """

        if title:
            title = f"❌ {title}"
        super().__init__(
            title=title,
            description=description,
            color=ERROR_COLOR,
            timestamp=utils.utcnow(),
        )
        self.set_footer(
            text=FOOTER_TEXT,
            icon_url=BotData.AVATAR_URL,
        )
