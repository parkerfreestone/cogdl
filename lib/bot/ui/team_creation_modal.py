from discord import ui
import aiohttp
import discord

# This needs to be better :thumbs_down:
API_BASE_URL = 'http://localhost:8000'

class TeamCreationModal(ui.Modal, title='Register Your Team'):
    name = ui.TextInput(label='Team Name', placeholder='Binturong', required=True)
    city = ui.TextInput(label='City', placeholder='Bismarck', required=True)
    primary_color = ui.TextInput(label='Primary Hex Color', placeholder='#afafaf', required=True)
    secondary_color = ui.TextInput(label='Secondary Hex Color', placeholder='#000000', required=True)
    stadium_name = ui.TextInput(label='Stadium Name', placeholder='Mf Trap House', required=True)

    async def on_submit(self, interaction: discord.Interaction):
        team_data = {
            "name": self.name.value,
            "city": self.city.value,
            "primary_color": self.primary_color.value,
            "secondary_color": self.secondary_color.value,
            "stadium_name": self.stadium_name.value,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(f"{API_BASE_URL}/teams", json=team_data) as response:
                if response == 200:
                    response_data = await response.json()
                    await interaction.response.send_message(f'{response_data["name"]}', ephemeral=True)
                else:
                    error_data = await response.text()
                    await interaction.response.send_message('Error creating team.', ephemeral=True)

        async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
            await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
            print(f"Error in TeamCreationModal: {str(error)}")