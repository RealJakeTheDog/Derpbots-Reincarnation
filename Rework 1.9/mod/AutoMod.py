import discord, asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot

Wdir = './BWords.txt'
Words = ['']

class AutoMod(commands.Cog, name='Moderator'): #NOT CURRRENTLY WORKING AS INTENDED
    def __init__ (self, bot):
        self.bot = bot
        self.words = Words

    @commands.Cog.listener(name='on_ready')
    async def CreateWords(self):
        self.words={}
        txt = open(Wdir, 'w+')
        Words = txt.read().strip().split(',')
        print(Words)

# Need to rework auto deleted words
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 804036103409369098:
            pass
        if Words == ['']:
            pass
        else:
            if any([word in message.content for word in Words]):
                if message.content.startswith('db!Whitelist'):
                    pass
                else:
                    await message.delete()
                    await message.channel.send(f'{message.author.mention}, You are not allowed to say that.')
            else:
                pass

    @commands.command()
    @has_permissions(manage_messages=True)
    async def Blacklist(self, ctx, arg):
        Words.append(arg)
        #txt.write(Words)
        await ctx.send(f'You have blacklisted the word {arg}. If you would like to undo this, run db!whitelist {arg}.')

    @commands.command()
    @has_permissions(manage_messages=True)
    async def Whitelist(self, ctx, arg):
        if any([word in arg for word in Words]):
            Words.remove(arg)
            await ctx.send(f'Whitelisted {arg}')
        else:
            await ctx.send(f'{arg} is not a blacklisted word.')

def setup(bot):
    bot.add_cog(AutoMod(bot))
