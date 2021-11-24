```py
import discord
from discord.ext import commands
import random
import secrets

prefix = "//"

bot = commands.Bot(command_prefix = prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
  print('loaded')

@bot.command()
async def roll(ctx, num=None):
    print(f'{ctx.author} | {ctx.author.id} -> //roll')
    result = secrets.randbelow(1000)
    if num is None:
        await ctx.send(content = ctx.message.author.mention + f"You need to provide a number. | Example: {prefix}roll 333")
        return
    if int(num) == int(result):
        await ctx.send(content = ctx.message.author.mention + "You won!")
    else:
        await ctx.send(content = ctx.message.author.mention + "You rolled **" + str(num) + "**. The correct number was **" + str(result) + "**. Keep trying! (0-1000)")
        
bot.run("BOT-TOKEN-HERE")
