import discord
from payday import bot1
from triads import bot2

token1 = "YOUR_TOKEN1_HERE"
token2 = "YOUR_TOKEN2_HERE"

bot2.login(token2)
bot1.login(token1)

bot1.run()
bot2.run()
