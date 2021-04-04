import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import sys, traceback

class HelpCMD(commands.HelpCommand):
    async def send_pages(self):
        destination=self.get_destination()
        for page in self.paginator.pages:
            embed=discord.Embed(description=page)
            await destination.send(embed=embed)
Help_Command=HelpCMD(no_category='Default Commands')
class config(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    async def BotConfig(self, ctx):
        commands.Bot(
            command_prefix='db!',
            case_insensitive=True,
            description='''
            A semi-useful, semi-stupid bot. For an invite link, do db!derpbot.
            ''',
            help_command= Help_Command
        )
def setup(bot):
    bot.add_cog(config(bot))
