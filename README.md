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

## Contributing

Contributions are welcome! Please read the contributing guide to get started.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
