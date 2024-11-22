from typing import Optional, Literal
from discord import utils


class BotData:
    VERSION: str = "BOT VERSION HERE"
    SUPPORT_SERVER: str = "SUPPORT SERVER HERE"
    AVATAR_URL: Optional[str] = None


OWNER_IDS = {
    418941954252996609,  # RejectModders
    379395029086633985,  # Joe?
    # Add more owner ids here
}

FOOTER_TEXT: str = f"FOOTER TEXT HERE"
COG_DIR: str = "cogs"  # The base directory of the cogs to be loaded
ALL_COGS: list[str] = []  # A list of all the cogs that have been loaded
LOG_DIR: str = "logs"  # The base directory of the logs to be stored
MAX_LOGS: int = 10  # The maximum number of logs to store
SYNC_GUILD_ID: int = GUILD ID HERE # The guild id for the sync command


BLACKLIST_LOG_CHANNEL: int = CHANNEL ID HERE
LOG_CHANNEL: int = CHANNEL ID HERE
BUG_REPORT_CHANNEL: int = CHANNEL ID HERE
SUGGESTION_CHANNEL: int = CHANNEL ID HERE
RELOAD_CHANNEL: int = CHANNEL ID HERE


# Colours -
MAIN_COLOR: int = 0x5865F2  # Blue
SUCCESS_COLOR: int = 0x00FF00  # Green
ERROR_COLOR: int = 0xFF0000  # Red

# Emoji Configurations - Find all of the Emojis in assets/emojis

# Green Check Mark
GREEN_CHECK: str = GO TO ASSETS/EMOJIS/DEFAULT AND ADD IT TO DISCORD
