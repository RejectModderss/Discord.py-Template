import discord
import datetime
import functools
import random

from discord.ext.commands import Context
from discord import Message
from typing import Optional, Callable, Union, TypeAlias
from utils import ErrorEmbed
from configurations.config import OWNER_IDS

OptionalUser: TypeAlias = Optional[Union[discord.Member, discord.User, int]]
OptionalCommand: TypeAlias = Optional[str]

cooldown_data = {"users": {}}
COOLDOWN_TEXTS = (
    "Chill, the command will be available {}",
    "What's the hurry? The command will be available {}.",
    "I appreciate your enthusiasm but the command can be used {}.",
    "Take a deep breath in, a deep breath out. The command will be available {}.",
)


class CoolDown:

    @staticmethod
    def cool_down(time: int, owner_bypass: bool = False):
        """
        A command decorator to handle cool downs and cool down replies automatically.
        @time: How long for the cool down to last in seconds
        @allow_bypass: Whether to allow bypassing the cooldown for owners. Optional and defaults to False
        """

        def decorator(func: Callable):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                nonlocal time

                context: Context = locals()["args"][1]
                cooldown_check = CoolDown.check(context)

                if cooldown_check[0] or (
                    owner_bypass and context.author.id in OWNER_IDS
                ):
                    CoolDown.add(time, context)
                    await func(*args, **kwargs)
                else:
                    cooldown_text = random.choice(COOLDOWN_TEXTS).format(
                        cooldown_check[1]
                    )
                    return await context.send(embed=ErrorEmbed(cooldown_text))

            return wrapper

        return decorator

    @staticmethod
    def add(
        time_: int,
        ctx_: Union[Context, Message],
        user: OptionalUser = None,
        command: OptionalCommand = None,
    ) -> None:
        """
        Adds the cool down to the user
        @command_: The command's name
        @ctx_ : The ApplicationContext of the user
        """

        if user is not None:
            assert isinstance(
                user, (discord.Member, discord.User, int)
            ), f"Expected [discord.Member, discord.User, int] instead got {type(user)}"

            if isinstance(user, (discord.Member, discord.User)):
                user = user.id
        else:
            user = ctx_.author.id
        command = ctx_.command.name if command is None else command
        current = datetime.datetime.now()

        cooldown_data["users"].setdefault(command, {})
        cooldown_data["users"][command][user] = current + datetime.timedelta(
            seconds=time_
        )

    @staticmethod
    def check(
        ctx_: Union[Context, Message],
        user: OptionalUser = None,
        command: OptionalCommand = None,
    ) -> tuple[bool, Optional[str]]:
        """
        Checks wheather the user is under a cool down or not
        @command_: The command's name
        @ctx_ : The ApplicationContext of the user
        """

        if user is not None:
            assert isinstance(
                user, (discord.Member, discord.User, int)
            ), f"Expected [discord.Member, discord.User, int] instead got {type(user)}"

            if isinstance(user, (discord.Member, discord.User)):
                user = user.id
        else:
            user = ctx_.author.id
        command = ctx_.command.name if command is None else command
        current = datetime.datetime.now()

        try:
            cooldown = cooldown_data["users"][command][user]
        except KeyError:
            return (True, None)

        if current > cooldown:
            try:
                del cooldown_data["users"][command][user]
            except KeyError:
                pass
            finally:
                return (True, None)

        else:
            cooldown = (
                f"<t:{round(cooldown_data['users'][command][user].timestamp())}:R>"
            )
            return (False, cooldown)

    @staticmethod
    def reset(
        ctx_: Union[Context, Message],
        user: OptionalUser = None,
        command: OptionalCommand = None,
    ) -> None:
        """
        Removes the cool down from the user
        @command_: The command's name
        @ctx_ : The ApplicationContext of the user
        """

        if user is not None:
            assert isinstance(
                user, (discord.Member, discord.User, int)
            ), f"Expected [discord.Member, discord.User, int] instead got {type(user)}"

            if isinstance(user, (discord.Member, discord.User)):
                user = user.id
        else:
            user = ctx_.author.id
        command = ctx_.command.name if command is None else command

        try:
            del cooldown_data["users"][command][user]
        except KeyError:
            pass
