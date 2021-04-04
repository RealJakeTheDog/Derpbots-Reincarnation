import discord
from discord.ext import commands
import asyncio
from discord.utils import get
from discord import member

class Counter(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_message(self, message):
        channel= self.bot.get_channel(810399359186763797)
        if message.channel == channel:
            msg = await channel.fetch_message(828112970868981760)
            number = int(msg.content) + 1
            await msg.edit(content=number)
            await message.delete()
        else:
            pass

def setup(bot):
    bot.add_cog(Counter(bot))
