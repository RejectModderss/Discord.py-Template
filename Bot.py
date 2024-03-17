import discord, config, asyncio, time, os, aiohttp
from discord.ext import commands, tasks
from pretty_help import PrettyHelp

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')




class Bot(commands.Bot, commands.AutoShardedBot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.reactions = True
        intents.typing = False
        intents.presences = True
        intents.guilds = True
        intents.invites = True
        self.db_connection = None

        super().__init__(command_prefix=config.Default_Prefix, intents=intents, help_command=PrettyHelp(),  strip_after_prefix=True, case_insensitive=True)



    async def setup_hook(self):
        """A function called when the bot logs in."""
        print(f'{self.user.name} has logged in successfully.')
        await self.load_extension('commands.cog_setup')
        self.loop.create_task(self.change_activity())


    async def change_activity(self):
        await self.wait_until_ready()

        while not self.is_closed():
            server_count = len(self.guilds)
            user_count = len(self.users)
            watching_activity = discord.Activity(name=f'over {user_count:,} users | {server_count:,} servers', type=discord.ActivityType.watching)
            living_life_activity = discord.Game(name='Living life', type=3)

            for activity in [watching_activity, living_life_activity]:
                if not self.is_ready():
                    return

                try:
                    await self.change_presence(activity=activity)
                except ConnectionResetError:
                    pass
                except discord.ConnectionClosed as e:
                    print(f"Connection closed. Reconnecting... ({e})")
                    await asyncio.sleep(5)

                await asyncio.sleep(60)



bot = Bot()

async def run1():
    await bot.start(TOKEN)

@bot.listen()
async def on_ready():
    print(f'{bot.user.name} is ready to recieve commands.')


