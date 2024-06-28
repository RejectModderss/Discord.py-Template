import discord
from discord.ext import commands, tasks

from core import Bot
from configurations.config import BotData


class StatusHandler(commands.Cog):
    """Cog for handling bot's dynamic status."""

    def __init__(self, bot: Bot):
        self.bot = bot
        self.status = None

    async def cog_load(self):
        self.status_task.start()
        print(f"{self.__class__.__name__} has been loaded.")

    async def cog_unload(self):
        self.status_task.cancel()
        print(f"{self.__class__.__name__} has been unloaded.")

    @tasks.loop(seconds=600.0)  # Changes status every 10 minutes
    async def status_task(self) -> None:
        await self.bot.wait_until_ready()

        if self.status is None:
            await self.__calculate_stats()

        try:
            current_status = next(self.status)
        except StopIteration:
            await self.__calculate_stats()
            current_status = next(self.status)

        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, name=current_status
            )
        )

    # Prefixed by double underscore means a private class method in python
    # Just a good practice for better code readabilty
    async def __calculate_stats(self) -> None:
        """Method for calculating bot stats. This is only executed on startup &
        when the bot is done iterating through all of its current statuses"""

        users = len(self.bot.users)
        guilds = len(self.bot.guilds)
        self.status = iter(
            # Prefixed by "Listening to"
            (
                f"running on version {BotData.VERSION}",
                f"over {users:,} users | {guilds:,} servers",
                f"/bugreport to report bugs",
            )
        )


async def setup(bot: Bot):
    await bot.add_cog(StatusHandler(bot))
