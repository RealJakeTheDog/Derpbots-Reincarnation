#Imports
import discord
import copy
import random
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import sys, traceback

Wdir = './Words.txt'

class HelpCMD(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination=self.get_destination()
        for page in self.paginator.pages:
            embed=discord.Embed(description=page)
            await destination.send(embed=embed)

Help_Command=HelpCMD(no_category='Default Commands')
bot = commands.Bot(
    command_prefix='db!',
    case_insensitive=True,
    description='''
    A semi-useful, semi-stupid bot. For an invite link, do db!derpbot.
    ''',
    help_command=Help_Command
)


initial_extensions = [
    'cogs.Useful',
    'cogs.Fun',
    'cogs.Music',
    'cogs.AutoMod-Blacklisted_Words',
    'cogs.AutoMod',
    'cogs.Config',
    'cogs.counter'
]
if __name__  == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print ('Started')
    print ('Username: ',end='')
    print (bot.user.name)
    print ('Userid: ',end='')
    print (bot.user.id)
    await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity('db!help'))

@bot.after_invoke
async def clean(ctx):
    try:
        message = ctx.message
        await message.delete()
    except:
        pass

#runs the bot and ensures that it stays online as long as the program is open
bot.run('', bot=True, reconnect=True)
