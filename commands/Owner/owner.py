import discord, config
from discord.ext import commands
from typing import *


class Bot_Admin(commands.Cog, name="Bot Admin"):
    """A set of commands only to used by the bot creators."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._last_result: Optional[Any] = None

    @commands.Cog.listener()
    async def on_ready(self):
        pass
    async def cog_load(self):
        print(f'{self.__class__.__name__} has been loaded.')

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
            sub_commands_count = len([subcommand.name for subcommand in self.bot.walk_commands() if subcommand.parent])

            embed = discord.Embed(
                title="Synchronization Complete",
                description=f"Synced {len(synced_global)} slash commands and {sub_commands_count} sub-commands globally.",
                timestamp=discord.utils.utcnow(),
                color=config.main_color
            )
            embed.set_footer(text="Footer text?", icon_url=self.bot.user.avatar.url)
            await ctx.send(embed=embed)
        # If an error occurs then send the error
        except Exception as e:
            embed = discord.Embed(title='❌ ERROR',
                                  description=f'**The error occured due to following reasons.\n```{e}```',
                                  color=config.error_color)
            embed.set_footer(text="Footer text?", icon_url=self.bot.user.avatar.url)
            await ctx.send(embed=embed)
            raise e