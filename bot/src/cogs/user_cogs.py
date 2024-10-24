from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv, find_dotenv
import aiohttp
import discord

import os

load_dotenv(find_dotenv())

API_BASE_URL = os.getenv("API_BASE_URL")

# A Cog to hold our team based commands
class UserCogs(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    # Allow users to register for the dodgeball league
    @app_commands.command()
    async def register(self, interaction: discord.Interaction):
        """Register an account with COGDL"""
        user_id = interaction.user.id
        user_name = interaction.user.name

        async with aiohttp.ClientSession() as session:
            payload = {"discord_id": str(user_id), "name": str(user_name)}

            async with session.post(f"{API_BASE_URL}/users/", json=payload) as response:
                if response.status == 201:
                    await interaction.response.send_message(
                        f"{interaction.user.mention}, Successfully registered",
                        ephemeral=True,
                    )
                else:
                    error_data = await response.json()
                    error_message = error_data.get(
                        "detail",
                    )
                    await interaction.response.send_message(
                        f"{interaction.user.mention}, Error registering - {error_message}",
                        ephemeral=True,
                    )


async def setup(bot):
    await bot.add_cog(UserCogs(bot))
