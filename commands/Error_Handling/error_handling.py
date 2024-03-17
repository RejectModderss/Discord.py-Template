import discord
from discord.ext import commands
import asyncio

class Error_Handle(commands.Cog):
    """Error Handling for commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        print(f'{self.__class__.__name__} has been loaded.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            missing_permissions = ", ".join(error.missing_permissions)
            embed = discord.Embed(title="Error", description=f"You don't have the necessary permissions to execute this command. Missing: {missing_permissions}", color=0xff0000)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.BotMissingPermissions):
            missing_permissions = ', '.join(error.missing_permissions)
            error_embed = discord.Embed(
                title='Error',
                description=f'I don\'t have the required permissions for this command, I need ``{missing_permissions}``',
                timestamp=discord.utils.utcnow(),
                color=0xff0000
            )
            await ctx.send(embed=error_embed)