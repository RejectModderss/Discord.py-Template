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


BLACKLIST_LOG_CHANNEL: int = CHANNEL ID HERE
LOG_CHANNEL: int = CHANNEL ID HERE
BUG_REPORT_CHANNEL: int = CHANNEL ID HERE
SUGGESTION_CHANNEL: int = CHANNEL ID HERE
RELOAD_CHANNEL: int = CHANNEL ID HERE


# Colours -
MAIN_COLOR: int = 0x5865F2  # Blue
SUCCESS_COLOR: int = 0x00FF00  # Green
ERROR_COLOR: int = 0xFF0000  # Red
