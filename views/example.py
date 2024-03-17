import discord, asyncio
from discord.ext import commands
import config
from config import error_color, success_color, main_color
import traceback


class Dropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='Apple', description='You picked Apple'),
            discord.SelectOption(label='Banana', description='You picked Banana'),
            discord.SelectOption(label='Orange', description='You picked Orange')
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Pick your favorite Fruit...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(f'You picked {self.values[0]}!')

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())

class SetColor(discord.ui.Modal, title='Color'):
    # Our modal classes MUST subclass `discord.ui.Modal`,
    # but the title can be whatever you want.

    # This is a longer, paragraph style input, where user can submit feedback
    # Unlike the name, it is not required. If filled out, however, it will
    # only accept a maximum of 300 characters, as denoted by the
    # `max_length=300` kwarg.
    feedback = discord.ui.TextInput(
        label='Enter the hex color.',
        style=discord.TextStyle.long,
        placeholder='Type the hex color here...',
        required=False,
        max_length=10,
    )

    async def on_submit(self, interaction: discord.Interaction):
        hex_color = self.feedback.value
        if hex_color.startswith('#'):
            hex_color = hex_color[1:]
        if len(hex_color) != 6 or not all(c in '0123456789ABCDEFabcdef' for c in hex_color):
            await interaction.response.send_message('Invalid hex color. Please enter a valid hex color.', ephemeral=True)
        else:
            await interaction.response.send_message(f'You have set the color as #{hex_color.upper()}', ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)

class ExampleText(discord.ui.Modal, title='Example Text'):
    message = discord.ui.TextInput(
        label='Enter the example text.',
        style=discord.TextStyle.long,
        placeholder='Type the example text here...',
        required=True,
        max_length=300,
    )
    color = discord.ui.TextInput(
        label='Enter the hex color.',
        style=discord.TextStyle.long,
        placeholder='Type the hex color here...',
        required=False,
        max_length=10,
    )

    async def on_submit(self, interaction: discord.Interaction):
        example_text = self.message.value
        hex_color = self.color.value
        if hex_color.startswith('#'):
            hex_color = hex_color[1:]
        if len(hex_color) != 6 or not all(c in '0123456789ABCDEFabcdef' for c in hex_color):
            await interaction.response.send_message('Invalid hex color. Please enter a valid hex color.', ephemeral=True)
        else:
            await interaction.response.send_message(f'You have set the example text as: {example_text} with color #{hex_color.upper()}', ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)


class BUTTONS(discord.ui.View):
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self.ctx = ctx
        self.pressed = False  # An attribute to check if a button is pressed or not
        self.embed_enabled = 0
        super().__init__(timeout=180)

    @discord.ui.button(label='Favorite Fruit', style=discord.ButtonStyle.blurple, row=0)
    async def set_profile(self, interaction: discord.Interaction, button: discord.ui.Button):
        # A check to see if the button user is same as command invoker
        if interaction.user != self.ctx.author:
            await interaction.response.send_message(
                content=f'You do not have the authority to use this button. Only the invoker of ``[command name here]`` command can use this button.\nInvoker for this command: {self.ctx.author.mention}',
                ephemeral=True)
            return

        # A check to see if a button is already pressed or not
        elif self.pressed is True:
            await interaction.response.send_message(
                content='Another button interaction is already going on. Please complete that first before pressing another button.',
                ephemeral=True)
            return

        # A check function to ensure the msg sender is same as button user and is sent as same channel
        # as the button pressed.
        def check(msg):
            return msg.author == interaction.user and msg.channel == interaction.channel

        # Initial Embed
        profile_em = discord.Embed(title="Favorite Fruit",
                                  color=main_color,
                                  description="Choose your favorite fruit.")
        view = DropdownView()
        await interaction.response.send_message(embed=profile_em, view=view)


    @discord.ui.button(label='Example Text', style=discord.ButtonStyle.blurple, row=0)
    async def set_welcome(self, interaction: discord.Interaction, button: discord.ui.Button):
        # A check to see if the button user is same as command invoker
        if interaction.user != self.ctx.author:
            await interaction.response.send_message(
                content=f'You do not have the authority to use this button. Only the invoker of ``[command name here]`` command can use this button.\nInvoker for this command: {self.ctx.author.mention}',
                ephemeral=True)
            return

        # A check to see if a button is already pressed or not
        elif self.pressed is True:
            await interaction.response.send_message(
                content='Another button interaction is already going on. Please complete that first before pressing another button.',
                ephemeral=True)
            return

        # A check function to ensure the msg sender is same as button user and is sent as same channel
        # as the button pressed.
        def check(msg):
            return msg.author == interaction.user and msg.channel == interaction.channel

        await interaction.response.send_modal(ExampleText())


    @discord.ui.button(label='Enable/Disable Example', style=discord.ButtonStyle.blurple, row=2)
    async def toggle(self, interaction: discord.Interaction, button: discord.ui.Button):
        # A check to see if the button user is same as command invoker
        if interaction.user != self.ctx.author:
            await interaction.response.send_message(
                content=f'You do not have the authority to use this button. Only the invoker of ``[command name here]`` command can use this button.\nInvoker for this command: {self.ctx.author.mention}',
                ephemeral=True)
            return

        # A check to see if a button is already pressed or not
        elif self.pressed is True:
            await interaction.response.send_message(
                content='Another button interaction is already going on. Please complete that first before pressing another button.',
                ephemeral=True)
            return

        if self.embed_enabled == 0:  # If embed is disabled
            self.embed_enabled = 1  # Set embed to enabled
            msg = await interaction.response.send_message(content="Enabled.")

        elif self.embed_enabled == 1:  # If embed is enabled
            self.embed_enabled = 0  # Set embed to disabled
            msg = await interaction.response.send_message(content="Disabled.")

