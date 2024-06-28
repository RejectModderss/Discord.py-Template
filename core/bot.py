import discord
import logging
import traceback

from discord.ext import commands

from utils import *
from configurations.default import DEFAULT_PREFIX
from configurations.config import MAIN_COLOR, BotData, OWNER_IDS
from pretty_help import PrettyHelp


class Bot(commands.Bot, commands.AutoShardedBot):
    def __init__(self, intents: discord.Intents):
        super().__init__(
            command_prefix=DEFAULT_PREFIX,
            intents=intents,
            help_command=PrettyHelp(),
            strip_after_prefix=True,
            case_insensitive=True,
            owner_ids=OWNER_IDS,
        )

    async def setup_hook(self):
        """A function called when the bot logs in."""

        BotData.AVATAR_URL = self.user.avatar.url
        print(f"{self.user.name} has logged in successfully.")

        # You can use this to change your bots profile to a gif later!

        # url = 'https://images.uni-bot.xyz/UniBot/UniBot%20Logo.gif'
        # async with aiohttp.ClientSession() as session:
        #     async with session.get(url) as resp:
        #         if resp.status != 200:
        #             print('Could not download file...')
        #         data = await resp.read()
        #
        # await self.user.edit(avatar=data)
