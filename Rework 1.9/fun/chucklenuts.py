import discord, discord.ext, random, asyncio
from discord.ext import commands, tasks


class Chucklenuts(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.randomizer.start()
    
    @tasks.loop(minutes=10)
    async def randomizer(self):
        chance=random.randint(1, 200)
        print(chance)
        if chance== 25:
            await Chucklenuts.thinkfast(self)
    @tasks.loop(seconds=7, count=30)
    async def piing(self, ping):
        channel=self.bot.get_channel(871142220848304138)
        async for message in channel.history(limit=10):
            if message.author == ping:
                fast = True
            else:
                fast = False
        if fast==True:
            await channel.send('POV: You thought fast.')
            self.piing.cancel()
        else:
            await channel.send(f'{ping.mention}')

    async def thinkfast(self):
        channel=self.bot.get_channel(871142220848304138)
        members = channel.guild.members
        ping = random.choice(members)
        if ping.bot == True:
            pass
        else:
            await channel.send('THINK FAST CHUCKLENUTS') 
            self.piing.start(ping)

    @commands.command(hidden=True)
    async def stopthepain(self, ctx):
        self.piing.cancel()

def setup(bot):
    bot.add_cog(Chucklenuts(bot))