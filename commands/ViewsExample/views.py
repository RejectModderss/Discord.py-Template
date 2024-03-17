import discord, random, config
from discord.ext import commands
from discord import app_commands
from views.example import DropdownView, BUTTONS


class Example(commands.Cog):
    """A set of commands that can be fun for everyone."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        pass

    async def cog_load(self):
        print(f'{self.__class__.__name__} has been loaded.')

    @commands.command()
    async def my_command(self, ctx: commands.Context):
        """Command to interact with buttons and views."""
        view = BUTTONS(self.bot, ctx)
        await ctx.send("Interact with the buttons below:", view=view)
