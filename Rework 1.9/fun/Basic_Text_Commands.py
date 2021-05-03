import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio
from time import sleep
import random
from random import choice


class Basic_Text_Commands(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Makes the bot say something')
    async def say(self, ctx, *, arg): #say command, makes the bot say something.
            await ctx.send(arg)
            await asyncio.sleep(0.3)

    @commands.command(brief='Despacito')
    async def despacito(self, ctx): #despacito command, makes the bot do despacito.
        await ctx.send('Did some carbon based life form just say ***DESPACITO***')

    @commands.command(brief='Power Manifested')
    async def deleteserver(self, ctx): #delete server, makes the bot say it deleted a server.
        print ('db!deleteserver')
        await ctx.send(ctx.author.mention + ' Has Deleted A Random Server')
        await ctx.send('I have used my power to delete a server. What server? I have no clue.')

    @commands.command(brief='Flips a coin')
    async def FlipACoin(self, ctx): #FlipACoin command, makes the bot flip a coin.
        coin = random.randint(1,2)
        if coin == 1:
            await ctx.send(':coin: It was heads.')
        if coin == 2:
            await ctx.send(':coin: It was tails.')


def setup(bot):
    bot.add_cog(Basic_Text_Commands(bot))
