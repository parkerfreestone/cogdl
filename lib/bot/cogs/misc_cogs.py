from discord.ext import commands
from discord import app_commands
import discord


class MiscCogs(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    # Sample command to use
    @app_commands.command()
    async def hello(self, interaction: discord.Interaction):
        """Says Hello!"""
        await interaction.response.send_message(f"Hello, {interaction.user.mention}!")


async def setup(bot):
    await bot.add_cog(MiscCogs(bot))
