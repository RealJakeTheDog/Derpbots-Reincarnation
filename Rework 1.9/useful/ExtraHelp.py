import discord
from discord.ext import commands
import asyncio


class ExtraHelp(commands.Cog, name='Useful'):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(name='DevMode', aliases=['ID'])
    async def DeveloperMode(self, ctx): #devmode command, shows user how to enable dev mode and get a channel ID.
        user = ctx.message.author
        await user.send('''To turn on developer mode, navagate to:
        `User Settings -> Advanced -> Developer Mode`
        If you\'re trying to get a channel id, right click the channel with developer mode on and click `copy ID`''')

def setup(bot):
    bot.add_cog(ExtraHelp(bot))
