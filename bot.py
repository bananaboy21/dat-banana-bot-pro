import discord
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix='*',description="dat banana bot, made by dat banana boi#1982.\n\nHelp Commands",owner_id=277981712989028353)


@bot.event
async def on_ready():
   print('Bot is online and READY TO ROLL!')
   
   
@bot.command()
async def ping(ctx):
    """Need ping pong? Get a websocket latency."""
    em = discord.Embed(color=discord.Color(value=0x00ff00))
    em.title = 'PoIIIIng! That was a whopping:'
    em.description = f'{bot.ws.latency * 1000:.4f} ms'
    await ctx.send(embed=em)
    
   

@bot.command()
async def textface(ctx, Type):
    """Get that lenny, tableflip or shrug face in here!"""
    if Type is None:
        await ctx.send('That is NOT a textface! Usage: *textface [lenny/tableflip/shrug]')
    else:
        if Type.lower() == 'lenny':
          await ctx.send('( ° ʖ °)')
        elif Type.lower() == 'tableflip':
          await ctx.send('(ノಠ益ಠ)ノ彡┻━┻')
        elif Type.lower() == 'shrug':
          await ctx.send('¯\_(ツ)_/¯')
        else:
          await ctx.send('That is NOT a textface! Usage: *textface [lenny/tableflip/shrug]')
            
            
@bot.command()
async def say(ctx, *, message: str):
    '''Yea, yea. I'll say what you say.'''
    await ctx.message.delete()
    await ctx.send(message)  
      
      
@bot.command()
async def invite(ctx):
    """Lemme in your server, mate. From here."""
    await ctx.send("Allow me to join the hood: https://discordapp.com/oauth2/authorize?client_id=389184269643153409&scope=bot&permissions=8 ")        

 
@bot.command()
async def discord(ctx):
    """Join our Discord server!"""
    await ctx.send("Your turn to enter the hood. https://discord.gg/wvkVknA")
    

if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
