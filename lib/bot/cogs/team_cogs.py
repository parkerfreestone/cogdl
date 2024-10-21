from lib.bot.ui.team_creation_modal import TeamCreationModal
from discord.ext import commands
from discord import app_commands
import discord

# A Cog to hold our team based commands
class TeamCogs(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    # Allow users to register a team in the league
    @app_commands.command()
    async def register_team(self, interaction: discord.Interaction):
        """Register your team"""
        await interaction.response.send_modal(TeamCreationModal())

    # Needs more work, should be a modal or something similar
    @app_commands.command()
    async def my_team(self, interaction: discord.Interaction):
        """View your team"""
        await interaction.response.send_modal(TeamCreationModal())

async def setup(bot):
    await bot.add_cog(TeamCogs(bot))