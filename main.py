import logging
import discord
import asyncio
import asyncpg
import os
import traceback


# haii :3
# i LOVE github merge conflict
from databases.base import BaseData
from datetime import datetime
from configurations.config import *
from core import Bot

from disckit import UtilConfig, CogEnum
from disckit.cogs import dis_load_extension

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def rotate_logs():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if os.path.exists("bot.log"):
        timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        new_log_name = f"{LOG_DIR}/{timestamp}.log"
        os.rename("bot.log", new_log_name)

        log_files = sorted(
            [f for f in os.listdir(LOG_DIR) if f.endswith(".log")],
            key=lambda x: os.path.getmtime(os.path.join(LOG_DIR, x)),
        )

        while len(log_files) > MAX_LOGS:
            os.remove(os.path.join(LOG_DIR, log_files.pop(0)))


rotate_logs()

logging.basicConfig(
    filename="bot.log",
    filemode="w",
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
    await bot.start(TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt detected.")
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
