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


BLACKLIST_LOG_CHANNEL: int = 1247953640765919282
LOG_CHANNEL: int = 1247953735120982078
BUG_REPORT_CHANNEL: int = 1247953803114844322
SUGGESTION_CHANNEL: int = 1247953864238563390
RELOAD_CHANNEL: int = 1247953919624347670


# Colours -
MAIN_COLOR: int = 0x5865F2  # Blue
SUCCESS_COLOR: int = 0x00FF00  # Green
ERROR_COLOR: int = 0xFF0000  # Red
