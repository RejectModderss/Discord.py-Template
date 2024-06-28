from discord.ext import commands
from core import Bot
from utils import *


class Bot_Admin(commands.Cog, name="Bot Admin"):
    """A set of commands only to used by the bot creators."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    async def cog_load(self):
        print(f"{self.__class__.__name__} has been loaded.")

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context):
        """
        Syncs all the commands to discord.

        **Usage:** sync
        """
        # Try to sync the commands
        try:
            synced_global = await ctx.bot.tree.sync()
            sub_commands_count = len(
                [
                    subcommand.name
                    for subcommand in self.bot.walk_commands()
                    if subcommand.parent
                ]
            )

            embed = MainEmbed(
                title="Synchronization Complete",
                description=f"Synced {len(synced_global)} slash commands and {sub_commands_count} sub-commands globally.",
            )
            await ctx.send(embed=embed)
        # If an error occurs then send the error
        except Exception as e:
            embed = ErrorEmbed(
                title="ERROR",
                description=f"**The error occured due to following reasons.\n```{e}```",
            )
            await ctx.send(embed=embed)
            raise e


async def setup(bot: Bot):
    await bot.add_cog(Bot_Admin(bot))
