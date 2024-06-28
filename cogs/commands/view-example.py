from discord.ext import commands
from discord import app_commands

from core.views.example import DropdownView, BUTTONS
from core import Bot


class Example(commands.Cog):
    """View Example on how the views work."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    async def cog_load(self):
        print(f"{self.__class__.__name__} has been loaded.")

    @commands.command()
    async def my_command(self, ctx: commands.Context):
        """Command to interact with buttons and views."""
        view = BUTTONS(self.bot, ctx)
        await ctx.send("Interact with the buttons below:", view=view)


async def setup(bot: Bot):
    await bot.add_cog(Example(bot))
