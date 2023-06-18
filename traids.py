import discord
from discord.ext import commands
from discord.ui.item import Item

intents = discord.Intents()
intents.message_content = True

bot = discord.Bot(command_prefix="/")  # Instantiate the Bot class from the discord module

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
    
bot.run("MTEwOTk5NzE0MTQ5MDkyOTY4NA.GqH6hU.uR-Tp_Kuz0FpOgE2ZwfsFUFDYZOtzZEE33Wwk4")