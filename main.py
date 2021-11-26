import discord
from discord.ext import commands
import random
import secrets

token = "BOT-TOKEN-HERE" # Replace BOT-TOKEN-HERE with your bot's token (get it at discord.com/developers)
prefix = "//" # Bot's prefix

bot = commands.Bot(command_prefix = prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
  print('loaded')

@bot.command()
async def roll(ctx, num=None):
    print(f'{ctx.author} | {ctx.author.id} -> {prefix}roll') # Logs whenever somebody uses the command
    result = secrets.randbelow(1000) # Change the number in () to change the max. generated number
    if num is None:
        await ctx.send(content = ctx.message.author.mention + f"You need to provide a number. | Example: {prefix}roll 333") # Error message for when the user doesn't choose any number
        return
    if int(num) == int(result):
        await ctx.send(content = ctx.message.author.mention + "You won!") # Win
    else:
        await ctx.send(content = ctx.message.author.mention + "You rolled **" + str(num) + "**. The correct number was **" + str(result) + "**. Keep trying! (0-1000)") # Lose
        
bot.run(token) # Runs the bot's token
