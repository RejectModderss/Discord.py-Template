from discord.ext import commands
from commands.Fun.fun_commands import Fun
from commands.Owner.owner import Bot_Admin



async def setup(bot:commands.Bot):
    await bot.add_cog(Fun(bot))
    await bot.add_cog(Bot_Admin(bot))
