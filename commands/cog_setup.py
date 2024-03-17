from discord.ext import commands
from commands.Fun.fun_commands import Fun
from commands.Owner.owner import Bot_Admin
from commands.ViewsExample.views import Example
from commands.Error_Handling.error_handling import Error_Handle



async def setup(bot:commands.Bot):
    await bot.add_cog(Fun(bot))
    await bot.add_cog(Bot_Admin(bot))
    await bot.add_cog(Example(bot))
    await bot.add_cog(Error_Handle(bot))
