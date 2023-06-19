import discord
from payday import bot1
from triads import bot2

token1 = "MTEwOTk5NzE0MTQ5MDkyOTY4NA.GqH6hU.uR-Tp_Kuz0FpOgE2ZwfsFUFDYZOtzZEE33Wwk4"
token2 = "MTEyMDA5ODAzNzI4MTMzMzM4OA.GOsraR.oNlbITGHy3PZ40pkjaEPY8fYnaFX_9jtjbphqU"

bot2.login(token1)
bot1.login(token2)

bot1.run()
bot2.run()
