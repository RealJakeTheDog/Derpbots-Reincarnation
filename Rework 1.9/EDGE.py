#Imports
import discord
import random
import logging
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot

class HelpCMD(commands.MinimalHelpCommand): #Set's the help command to use embeds. You can also use this to make the help command look nicer but for now it's just basic embed
    async def send_pages(self):
        destination=self.get_destination()
        for page in self.paginator.pages:
            embed=discord.Embed(Title='Derpbot', description=page)
            await destination.send(embed=embed)

logging.basicConfig(level=logging.INFO)
intents=discord.Intents.all()
Help_Command=HelpCMD(no_category='Default Commands') #set's the help command to the minimal help command class
bot = commands.Bot(
    command_prefix='db!',
    case_insensitive=True,
    description='''
    A semi-useful, semi-stupid bot. For an invite link, do db!derpbot.
    ''',
    help_command=Help_Command,
    intents=intents
)


initial_extensions = [
    'bot.extHUB', #Cog used to load everything else. The reason I did it this way was so it was easier to handle errors and so that the bot can't insta crash.
    'bot.errorHandler', #Error handler, brand new so not very good but it does work.
    'useful.Music'
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

@bot.command(brief = 'A small intro to the bot, including the invite link')
async def derpbot(ctx):
    await ctx.send('I am the reincarnation of the once powerful Derpbot (Invite link: https://bit.ly/2YmxOfw) ')

@bot.after_invoke #delete's original command message after the command has been executed.
async def clean(ctx):
    try:
        message = ctx.message
        await message.delete()
    except:
        pass

#runs the bot and ensures that it stays online as long as the program is open
bot.run('ODA0MDM2MTAzNDA5MzY5MDk4.YBGe-Q.ei3HVRjk85pZMT-ivSN2rfpNhnU', bot=True, reconnect=True)
