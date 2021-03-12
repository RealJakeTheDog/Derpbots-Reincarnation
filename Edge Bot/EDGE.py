#Imports
import discord
import copy
import random
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import sys, traceback

Wdir = ('./Words.csv')

help_command = commands.DefaultHelpCommand(no_category = 'Commands')
#creating a new discord client
bot = commands.Bot(command_prefix='db!', case_insensitive = True, description='A semi-useful, semi-stupid bot. For an invite link, do db!derpbot.', help_command=help_command)

#loads cogs (Multi File Commands)
initial_extensions = [
    'cogs.Admin',
    'cogs.Useful',
    'cogs.Fun',
    'cogs.Music',
    'cogs.AutoMod-Blacklisted_Words',
    'cogs.AutoMod'
]
if __name__  == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

#Prints After Successful start
@bot.event
async def on_ready():
    print ('Started')
    print ('Username: ',end='')
    print (bot.user.name)
    print ('Userid: ',end='')
    print (bot.user.id)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('db!help') )
    try:
        with open(Wdir, 'x') as csv_filie:
            pass
    except:
        pass

@bot.command(brief = 'Changes the status of the bot')
async def status(self, ctx, *, args):
    await bot.change_presence(status = discord.Status.online, activity=discord.Game(args))
    await ctx.send('Online Status Has Been Changed To'+ args)

@bot.command()
async def reload(ctx, arg):
    id = str(ctx.author.id)
    if id == '395269984374489089':
        try:
            bot.reload_extension(arg)
            await ctx.send(f'Reloaded {arg}')
        except:
            await ctx.send(f'Was unable to reload {arg}, please try again.')
    else:
        await ctx.send('No')
@bot.command()
async def load(ctx, arg):
    id = str(ctx.author.id)
    if id == '395269984374489089':
        try:
            bot.load_extension(arg)
            await ctx.send(f'Loaded {arg}.')
        except:
            await ctx.send(f'Unable to load {arg}.')
    else:
        await ctx.send('No')

@bot.command()
async def unload(ctx, arg):
    id = str(ctx.author.id)
    if id == '395269984374489089':
        try:
            bot.unload_extension(arg)
            await ctx.send(f'Unloaded {arg}.')
        except:
            await ctx.send(f'Unable to unload {arg}.')

@bot.command()
async def Close(ctx):
    id = str(ctx.author.id)
    if id == '395269984374489089':
        await bot.logout()
    else:
        await ctx.send('No')




#runs the bot and ensures that it stays online as long as the program is open
bot.run('API KEY GOES HERE', bot=True, reconnect=True)
