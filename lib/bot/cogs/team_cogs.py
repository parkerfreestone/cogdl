from discord.ext import commands
from discord import app_commands
from lib.bot.ui.team_creation_modal import TeamCreationModal
import discord

class TeamCogs(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @app_commands.command()
    async def register_team(self, interaction: discord.Interaction):
        """Register your team"""
        await interaction.response.send_modal(TeamCreationModal())

    @app_commands.command()
    async def my_team(self, interaction: discord.Interaction):
        """View your team"""
        await interaction.response.send_modal(TeamCreationModal())

async def setup(bot):
    await bot.add_cog(TeamCogs(bot))