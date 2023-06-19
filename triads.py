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

#start of clean/dirty
@bot.slash_command(description="Add 20% to a value which is good for calculating clean cash to dirty")
async def dirty(ctx, value: float):
    new_value = value * 1.2
    await ctx.respond(f"The new value is {new_value:.2f}")

@bot.slash_command(description="Remove 20% to a value which is good for calculating dirty to clean cash")
async def clean(ctx, value: float):
    new_value = value / 1.2
    await ctx.respond(f"The new value is {new_value:.2f}")

#maths
@bot.slash_command(description="adds two values")
async def sum(ctx, a: int, b: int):
  await ctx.respond(a + b)

@bot.slash_command(description="multiplys two values")
async def multiply(ctx, a: int, b: int):
  await ctx.respond(a * b)

@bot.slash_command(description="minuses two values")
async def minus(ctx, a: int, b: int):
  await ctx.respond(a - b)
  
@bot.slash_command(description="divides two values")
async def divide(ctx, a: int, b: int):
  await ctx.respond(a / b)

#purge
@bot.slash_command(pass_context=True, descirption="Purge an amount of messages")
@commands.has_role("The Family")
async def purge(ctx, limit: int):
    try:
        if limit > 20:
            limit = 20
        await ctx.channel.purge(limit=limit+1)
        await ctx.send(f"{limit} messages deleted.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.slash_command(descirption="The commands that we have")
async def help(ctx):
    embed = discord.Embed(
        
        title="Triad Help",
        description="The following commands are what you can use in order to improve your experience in our discord",
        color=discord.Colour.yellow(), # Pycord provides a class with default colors you can choose from
        
    )
    embed.add_field(name="/dirty", value="Add '20%' to a value", inline=True)
    embed.add_field(name="/ping", value="Sends the bot's latency", inline=True)
    embed.add_field(name="/clean", value="Takes away '20%' from a value" , inline=True)
    embed.add_field(name="/multiply", value="Multiplys two values", inline=True)
    embed.add_field(name="/add", value="Adds two values", inline=True)
    embed.add_field(name="/divide", value="Divides two values", inline=True)
    embed.add_field(name="/minus", value="Minuses two values", inline=True)
 
    embed.set_footer(text="Bot created by Camerinio.") # footers can have icons too
    embed.set_author(name="Payday", icon_url="")
    embed.set_thumbnail(url="https://i.imgur.com/6zMSFoM.png")
    embed.set_image(url="https://i.imgur.com/6zMSFoM.png")
 
    await ctx.respond(embed=embed) # Send the embed with some text")

    
bot.run("MTEyMDA5ODAzNzI4MTMzMzM4OA.GOsraR.oNlbITGHy3PZ40pkjaEPY8fYnaFX_9jtjbphqU")