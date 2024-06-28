import discord
import traceback

from discord.ui import View
from typing import Optional

from utils import ErrorEmbed


class BaseView(View):
    """A custom base view which extends`discord.ui.View`
    to provide more inbuilt features."""

    def __init__(
        self,
        author: Optional[int] = None,
        disable_on_timeout: bool = True,
        *args,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        author: Optional[:class:`int`], default `None`
            The author of the `View`. If set to `None` anyone can interact with the `View`.
        disable_on_timeout: :class:`bool`, default `True`
            If set to `True` it will disable all items in the view when it times out.
        """

        super().__init__(*args, **kwargs)

        self.message: Optional[discord.Message] = None
        self._author = author
        self._disable_on_timeout = disable_on_timeout

    def disable_all_items(self) -> bool:
        """Disables all items in the View when called."""
        for item in self.children:
            item.disabled = True

    async def on_timeout(self) -> None:
        if self._disable_on_timeout:
            self.disable_all_items()
            if self.message:
                try:
                    await self.message.edit(view=self)
                except discord.errors.NotFound:
                    pass
            else:
                traceback.print_stack()
                raise Warning("BaseView.message was not defined to disable the items.")

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if self._author is None:
            return True

        if interaction.user.id != self._author:
            await interaction.response.send_message(
                embed=ErrorEmbed("This interaction is not for you!"), ephemeral=True
            )
            return False
        return True
