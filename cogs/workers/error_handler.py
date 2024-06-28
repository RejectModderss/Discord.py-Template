import discord
import traceback
import sys

from discord.ext import commands

from core import Bot
from configurations import config
from utils import *


class ErrorHandler(commands.Cog, name="Error Handler"):
    """Error Handling for commands"""

    def __init__(self, bot: Bot):
        self.bot = bot

    async def cog_load(self):
        print(f"{self.__class__.__name__} has been loaded.")

    async def throw_err(self, ctx: commands.Context, error: discord.DiscordException):
        print(f"Ignoring exception in command {ctx.command}:", file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr
        )

        channel = self.bot.get_channel(config.LOG_CHANNEL)
        if channel is None:
            channel = await self.bot.fetch_channel(config.LOG_CHANNEL)

        if channel is not None:
            await channel.send(
                embed=ErrorEmbed(
                    f"```\nError caused by-\nAuthor Name: {ctx.author}"
                    f"\nAuthor ID: {ctx.author.id}\n"
                    f"\nError Type-\n{type(error)}\n"
                    f"\nError Type Description-\n{error.__traceback__.tb_frame}\n"
                    f"\nCause-\n{error.with_traceback(error.__traceback__)}```",
                    f"Error in command: {ctx.command.name}",
                )
            )
        await ctx.reply(
            embed=ErrorEmbed(
                title="Sorry...",
                description="An unexpected error has occurred. The developers have been notified of it.",
            )
        )

    @commands.Cog.listener()
    async def on_command_error(
        self, ctx: commands.Context, error: discord.DiscordException
    ) -> None:
        if isinstance(ctx.channel, discord.DMChannel):
            return

        if isinstance(error, commands.CommandNotFound):
            return

        elif (
            isinstance(error, commands.CommandError)
            and str(error) == "User is blacklisted."
        ):
            return

        elif isinstance(error, discord.NotFound):
            if error.code == 10008:
                return

        elif isinstance(error, commands.errors.NotOwner):
            error_embed = ErrorEmbed(
                title="Error",
                description="You do not have the required permissions to use this command.\n"
                "This command is only available to owners!",
            )
            await ctx.send(embed=error_embed, ephemeral=True)

        elif isinstance(error, commands.MissingRequiredArgument):
            param = error.param.name
            command = ctx.command
            description = command.help or "No description available."

            embed = MainEmbed(
                title="Information", description=f"Missing Argument: `{param}`"
            )
            embed.set_thumbnail(url="https://images.uni-bot.xyz/UniBot/missing_arg.png")
            embed.add_field(name="Description", value=description, inline=False)
            await ctx.send(embed=embed, ephemeral=True)

        elif isinstance(error, commands.BotMissingPermissions):
            missing_permissions = ", ".join(error.missing_permissions)
            error_embed = ErrorEmbed(
                title="Error",
                description=f"I don't have the required permissions for this command, "
                f"I need ``{missing_permissions}`` permission to proceed with this command.",
            )
            error_embed.set_thumbnail(
                url="https://images.uni-bot.xyz/UniBot/Missing_perms.png"
            )
            await ctx.send(embed=error_embed, ephemeral=True)

        elif isinstance(error, commands.errors.MissingPermissions):

            missing_permissions = ", ".join(error.missing_permissions)
            error_embed = ErrorEmbed(
                title="Error",
                description=f"You don't have the required permissions for this command, "
                f"you need ``{missing_permissions}`` permission to use this command.",
            )
            error_embed.set_thumbnail(
                url="https://images.uni-bot.xyz/UniBot/Access_Denied.png"
            )
            await ctx.send(embed=error_embed, ephemeral=True)

        elif isinstance(
            error, (commands.CommandInvokeError, commands.errors.HybridCommandError)
        ):
            original = getattr(error, "original", error)
            if isinstance(original, discord.Forbidden):
                member = ctx.message.mentions[0] if ctx.message.mentions else None

                if member:
                    if ctx.author.top_role < member.top_role:
                        error_embed = ErrorEmbed(
                            title="Error",
                            description="You cannot perform this action due to role hierarchy.",
                        )
                        await ctx.send(embed=error_embed, ephemeral=True)
                    elif ctx.guild.me.top_role <= member.top_role:
                        error_embed = ErrorEmbed(
                            title="Error",
                            description="I cannot perform this action due to role hierarchy.",
                        )
                        await ctx.send(embed=error_embed, ephemeral=True)

        elif isinstance(
            error, (commands.ChannelNotFound, commands.errors.ChannelNotFound)
        ):
            error_embed = ErrorEmbed(
                title="Error",
                description=f"The specified channel {error.argument} was not found."
                "Please pass in a valid channel.",
            )
            await ctx.send(embed=error_embed)

        # elif isinstance(error.original, asyncio.tasks.Task):
        #     return

        else:
            await self.throw_err(ctx=ctx, error=error)


async def setup(bot: Bot):
    await bot.add_cog(ErrorHandler(bot))
