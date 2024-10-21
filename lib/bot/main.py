from dotenv import load_dotenv
from discord.ext import commands
import logging
import discord
import asyncio
import os

load_dotenv()

DEFAULT_GUILD = os.getenv("GUILD_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")

EXTENSIONS = ('cogs.misc_cogs', 'cogs.team_cogs',)
INTENTS = discord.Intents.default()
INTENTS.message_content = True

# Logger config (Should prob be moved to it's own file since it's ugly as fuck)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(
        command_prefix='!',
        intents=INTENTS
    )

# Loads our cogs "or extentions if you're cringe 🤓"
@bot.event
async def setup_hook():
    for extension in EXTENSIONS:
        await bot.load_extension(extension)

# Runs when our bot starts up
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Syncs all commands from global context to a specified guild
@bot.command()
async def sync(ctx):
    bot.tree.copy_global_to(guild=discord.Object(id=DEFAULT_GUILD))

    synced_commands = await bot.tree.sync(guild=discord.Object(id=DEFAULT_GUILD))
    print(f'synced {[command.name for command in synced_commands]} commands')

async def main():
    async with bot:
        await bot.start(BOT_TOKEN)

if __name__ == '__main__':
    asyncio.run(main())