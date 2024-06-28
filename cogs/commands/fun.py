import random

from discord.ext import commands
from discord import app_commands

from core.functions.fun_cmds import RPS_Choices
from core import Bot
from utils import *


class Fun(commands.Cog):
    """A set of commands that can be fun for everyone."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    async def cog_load(self):
        print(f"{self.__class__.__name__} has been loaded.")

    # This is a hybrid group command.
    # It can be used as a normal command or as a group command.
    # Which means you have sub commands with this group.

    @commands.hybrid_group(
        name="fun",
        invoke_without_command=True,
        strip_after_prefix=True,
        case_insensitive=True,
    )
    @commands.guild_only()
    async def fun_cmd(self, ctx):
        """
        Base fun commands.
        """

    @fun_cmd.command(name="coinflip")
    @commands.guild_only()
    async def coinflip(self, ctx):
        """
        Play coin flip.

        **Usage:** coinflip
        """

        chance = random.randint(1, 100)

        if chance <= 5:
            result = "Side"
        else:
            result = random.choice(["Heads", "Tails"])
        coinflip_url = "https://images.uni-bot.xyz/UniBot/gq4Irp4.gif"
        embed = MainEmbed(
            title="Coinflip",
            description=f"The coin landed on: `{result}`",
        )
        embed.set_thumbnail(url=coinflip_url)

        await ctx.send(embed=embed)

    @fun_cmd.command(name="dice")
    @commands.guild_only()
    @app_commands.describe(dice="Amount of dice.")
    @app_commands.describe(sides="Amount of sides.")
    async def dice(self, ctx, dice: int, sides: int):
        """
        Roll the dice.

        **Usage:** dice [dice] [sides]

        **Examples:**
        - `dice 10 69`
        """
        if dice <= 0 or sides <= 1:
            error_embed = ErrorEmbed(
                title="Invalid Parameters",
                description="Please provide valid values for the number of dice and sides (both must be greater than 0).\n\nMake sure sides is greater than 1 tho!",
            )
            await ctx.send(embed=error_embed)
            return

        if dice > 10:
            error_embed = ErrorEmbed(
                title="Too Many Dice",
                description="You can roll up to 10 dice at a time for performance reasons.",
            )
            await ctx.send(embed=error_embed)
            return

        if sides > 1000:
            error_embed = ErrorEmbed(
                title="Too Many Sides",
                description="The number of sides on a dice cannot exceed 1000.",
            )
            await ctx.send(embed=error_embed)
            return

        dice_rolls = [random.randint(1, sides) for _ in range(dice)]
        total = sum(dice_rolls)

        roll_description = ", ".join(map(str, dice_rolls))
        result_embed = MainEmbed(
            title=f"Dice Roll - {dice}d{sides}",
            description=f"**Rolls**: {roll_description}\n**Total**: {total}",
        )
        await ctx.send(embed=result_embed)

    @fun_cmd.command(name="rps")
    @commands.guild_only()
    @app_commands.describe(user_choice="The choice of Rock, Paper or Scissors.")
    async def rps(self, ctx, user_choice: RPS_Choices):
        """
        Play Rock, Paper, Scissors with the bot!

        **Usage:** rps [user_choice]

        **Examples:**
        - `rps Rock`
        """
        await ctx.defer()

        choices = [RPS_Choices.rock, RPS_Choices.paper, RPS_Choices.scissors]
        bot_choice = random.choice(choices)

        if user_choice == bot_choice:
            result = "It's a tie!"
            embed = ErrorEmbed(
                title="Rock, Paper, Scissors",
                description=result,
            )
        elif (
            (user_choice == RPS_Choices.rock and bot_choice == RPS_Choices.scissors)
            or (user_choice == RPS_Choices.paper and bot_choice == RPS_Choices.rock)
            or (user_choice == RPS_Choices.scissors and bot_choice == RPS_Choices.paper)
        ):
            result = f"You win! {ctx.author.mention} chose {user_choice.name.lower()}, and I chose {bot_choice.name.lower()}."
            embed = SuccessEmbed(
                title="Rock, Paper, Scissors",
                description=result,
            )
        else:
            result = f"I win! {ctx.author.mention} chose {user_choice.name.lower()}, and I chose {bot_choice.name.lower()}."
            embed = ErrorEmbed(
                title="Rock, Paper, Scissors",
                description=result,
            )

        await ctx.send(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Fun(bot))
