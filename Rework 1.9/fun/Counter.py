import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio
from time import sleep


class counter(commands.Cog):
    def __init__ (self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_message(self, message): #Counter command, causes the bot to count by 1 every message that is sent in the counting channel
        if message.author.id == 804150363602419782:
            pass
        else:
            channel = discord.utils.get(message.guild.channels, id=810399359186763797)
            if message.channel == channel:
                lastmsg = channel.last_message
                print(lastmsg.content)
                if message.content == (int(lastmsg.content)+1):
                    pass
                else:
                    await message.delete()

def setup(bot):
    bot.add_cog(counter(bot))
