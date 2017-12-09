import discord
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix='*',description="dat banana bot, made by dat banana boi#1982.\n\nHelp Commands",owner_id=277981712989028353)


@bot.event
async def on_ready():
   print('Bot is online!')
   
   
@bot.command()
async def ping(ctx):
    """Need ping pong? Get a websocket latency."""
    em = discord.Embed(color=discord.Color(value=0x00ff00))
    em.title = 'PoIIIIng! That was a whopping:"
    em.description = f'{bot.ws.latency * 1000:.4f} ms'
    await ctx.send(embed=em)
    
    

if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
