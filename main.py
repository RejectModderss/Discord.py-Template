import logging
import discord
import asyncio
import asyncpg
import os
import threading
import traceback


# hi
import tokens
from databases.base import BaseData
from configurations.config import COG_DIR
from core import Bot

logging.basicConfig(
    filename="bot.log",
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)s [%(lineno)d] %(message)s",
)
logging.getLogger("httpx").setLevel(logging.ERROR)

logging.getLogger("googleapiclient.discovery_cache").setLevel(logging.ERROR)
logging.getLogger("werkzeug").setLevel(logging.ERROR)


async def load_cogs(bot: Bot) -> None:
    """A function for loading cogs from the base cog directory."""

    for folder in os.listdir(COG_DIR):
        for cog in os.listdir(COG_DIR + "/" + folder):
            if cog.endswith(".py"):
                cog_path = COG_DIR + "." + folder + "." + cog[:-3]
                try:
                    await bot.load_extension(cog_path)
                except Exception as e:
                    print(f"Failed to load extension {cog_path}. Error: {e}")
                    traceback.print_exc()


async def main():
    discord.utils.setup_logging()

    intents = discord.Intents.all()
    intents.typing = False
    intents.guild_scheduled_events = False

    # BaseData.db_connection = await asyncpg.create_pool(
    #     host=tokens.HOST,
    #     database=tokens.DATABASE_NAME,
    #     port=tokens.PORT,
    #     user=tokens.USER,
    #     password=tokens.PASSWORD,
    #     max_inactive_connection_lifetime=0,
    # )
    #
    # print("Connected to database")
    #
    # async with BaseData.db_connection.acquire() as connection:
    #     for schema in os.listdir("schemas/"):
    #         with open(f"schemas/{schema}", "r") as sql:
    #             await connection.execute(sql.read())

    bot = Bot(intents=intents)
    await load_cogs(bot=bot)
    await bot.start(tokens.TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt detected.")
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
