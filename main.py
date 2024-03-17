import logging
from Bot import bot
import discord
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv('TOKEN')

async def main():
  discord.utils.setup_logging()

  await bot.start(TOKEN)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    logging.info("KeyboardInterrupt detected.")
except Exception as e:
    logging.exception("An error occurred: ")