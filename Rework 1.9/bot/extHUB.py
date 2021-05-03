import discord
import discord.ext
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio

Defualt_Extensions=[ #Cogs to load on launch
    'useful.Color',
    'useful.ExtraHelp',
    'useful.Polls',
    'mod.AutoMod',
    'mod.Text_Commands',
    'mod.User_Commands',
    'fun.Basic_Text_Commands',
    'fun.InsultPlus',
    'useful.Music',
    'admin.Admin',
    'lfg.VC'
]

class extensionclass(commands.Cog, name='Extensions'):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ReloadAll(self, ctx):
        for extension in bot.cogs():
            self.bot.reload_extension(extension)
            print(f'Loaded {extension}')

    @commands.Cog.listener()
    async def on_ready(self): #Loads Cogs in Default_Extensions
        for extension in Defualt_Extensions:
            self.bot.load_extension(extension)
            print(f'Loaded {extension}')
def setup(bot):
    bot.add_cog(extensionclass(bot))
