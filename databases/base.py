from typing import Optional
from asyncpg import Pool
import logging
import traceback


logger = logging.getLogger(__name__)


class BaseData:
    """A class representing the base of all databases connected via Postgresql."""

    db_connection: Optional[Pool] = None

    def __new__(cls, *args, **kwargs):
        if cls.db_connection is not None:
            if cls.db_connection.is_closing():
                traceback.print_stack()
        else:
            logger.info("Database is not connected.")

        assert cls.db_connection is not None, "Database is not connected."
        assert (
            not cls.db_connection.is_closing()
        ), "Database connection is closed / closing."

        return super().__new__(cls, *args, **kwargs)
