# Discord Bot Template

This is a template for creating a Discord bot using Python and the discord.py library. It features a modular design with cogs for easy addition and removal of features.

## Features

- Cog-based structure for easy management of commands.
- Owner-only commands for bot management.
- Command synchronization with Discord.
- Uses sub commands in the cog `Fun`.
- Shows buttons and drop downs!

## Installation

1. Clone the repository: `git clone https://github.com/RejectModderss/Discord.py-Template`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add your bot token like so:
    ```
    TOKEN = 'YOUR BOT TOKEN HERE'
    ```
4. Run the bot: `python main.py`

## Usage

### Cogs

The bot uses a cog-based structure. Each cog represents a category of commands. You can add your own cogs to extend the bot's functionality.

### Commands

The bot has a variety of commands. Here are some examples:

- `sync`: This command, available only to the bot owner, syncs all the bot's commands with Discord.

### Other Info

Everything inside of this bot is from `discord.py 2.3.2` if you have errors, please make sure you are on the right version of dpy!

I made this because others don't know cogs or don't know how to use buttons/drop downs!

If you need help, add me on discord `rejectmodders`! 
