import discord
from discord.ext import commands
from discord.ui.item import Item

intents = discord.Intents()
intents.message_content = True

client = discord.client(command_prefix="/")  # Instantiate the client class from the discord module

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print('------')

@client.command(description="Sends the client's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {client.latency}")

# Slash Command: Dirty
@client.slash_command(descirption="Add 20% to a value which is good for calculating clean cash to dirty")
async def dirty(ctx, value: float):
    new_value = value * 1.2
    await ctx.respond(f"The new value is {new_value:.2f}")

# Command: Prices
@client.slash_command(description="What Payday buys bank equipment for")
async def prices(ctx):
    response = "**Thermal:** 40-60k\n**Thermite:** 15-20k\n**Level 3 Access Card:** 25-35k\n**Level 6 Access Card:** 40-60k\n"
    await ctx.respond(response)

@client.slash_command(description="adds two values")
async def sum(ctx, a: int, b: int):
  await ctx.respond(a + b)

@client.slash_command(description="multiplys two values")
async def multiply(ctx, a: int, b: int):
  await ctx.respond(a * b)

@client.slash_command(description="minuses two values")
async def minus(ctx, a: int, b: int):
  await ctx.respond(a - b)
  
@client.slash_command(description="divides two values")
async def divide(ctx, a: int, b: int):
  await ctx.respond(a / b)
  
class MyView(discord.ui.View):
    def __init__(self):
       super().__init__()
       self.value = None
       
    @discord.ui.button(label="Colour", row=0, style=discord.ButtonStyle.primary, emoji="<a:CCpepe_robber:1067803612526419978>")
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message("#D2B48C")

    @discord.ui.button(label="Database", row=0, style=discord.ButtonStyle.green, emoji="<:payday1:1067813079527723008>")
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message("https://docs.google.com/spreadsheets/d/12REsqTwWxpcQx6r94-8u9JZ1PVcIdNZioJZLbe36bO8/edit?usp=sharing")
    
    @discord.ui.button(label="Radio", row=0, style=discord.ButtonStyle.red, emoji="📻")
    async def third_button_callback(self, button, interaction):
        await interaction.response.send_message("Join Radio 766")
    
    @client.slash_command(description="Important Payday information") # Create a slash command
    @commands.has_role("Gang member")
    async def important(ctx):
        await ctx.respond("Important information", view=MyView()) # Send a message with our View class that contains the button

class MyView1(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Merchant", row=0, style=discord.ButtonStyle.green, emoji="💰")
    async def first_button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        member = interaction.user
        role = discord.utils.get(interaction.guild.roles, name="Merchant")
        await member.add_roles(role)
        await interaction.response.send_message("You have now received the Merchant role.", ephemeral=True)


    @discord.ui.button(label="Contractor", row=0, style=discord.ButtonStyle.green, emoji="🏎️")
    async def second_button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        member = interaction.user
        role = discord.utils.get(interaction.guild.roles, name="Contractor")
        await member.add_roles(role)
        await interaction.response.send_message("You have now received the Contractor role.", ephemeral=True)

@client.event
async def on_ready():
    # Get the desired channel where you want to send the message
    channel = client.get_channel(1102730487379808326)

    # Send the message with your view class
    view = MyView1()
    message = await channel.send("React to receive your role.", view=view)

@client.slash_command()
async def roles(ctx):
    await ctx.respond("Role request", view=MyView1())
    
@client.command(pass_context=True)
@commands.has_role("Controller")
async def purge(ctx, limit: int):
    try:
        if limit > 20:
            limit = 20
        await ctx.channel.purge(limit=limit+1)
        await ctx.send(f"{limit} messages deleted.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@client.command()
async def help(ctx):
    embed = discord.Embed(
        
        title="Payday Help",
        description="The following commands are what you can use in order to improve your experience in our discord",
        color=discord.Colour.yellow(), # Pycord provides a class with default colors you can choose from
        
    )
    embed.add_field(name="/dirty", value="Add 20% to a value", inline=True)
    embed.add_field(name="/ping", value="Sends the client's latency", inline=True)
    embed.add_field(name="/prices", value="Bank equipment prices", inline=True)
    embed.add_field(name="/multiply", value="Multiplys two values", inline=True)
    embed.add_field(name="/add", value="Adds two values", inline=True)
    embed.add_field(name="/divide", value="Divides two values", inline=True)
    embed.add_field(name="/minus", value="Minuses two values", inline=True)
 
    embed.set_footer(text="client created by Camerinio.") # footers can have icons too
    embed.set_author(name="Payday", icon_url="")
    embed.set_thumbnail(url="https://i.imgur.com/6F4vy46.png")
    embed.set_image(url="https://i.imgur.com/vvMxzUL.png")
 
    await ctx.respond(embed=embed) # Send the embed with some text


client.run("MTEwOTk5NzE0MTQ5MDkyOTY4NA.GfiCxK.LjbPRZbIB0hlGoIOB-gRnqE5NUYJPlNrkGqdYU")