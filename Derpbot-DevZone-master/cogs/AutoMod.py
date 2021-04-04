import discord
from discord.ext import commands
from time import sleep
from discord.utils import get
from discord.ext.commands import Bot
import csv
import re
import asyncio
from discord.ext.commands import has_permissions, CheckFailure

Wdir = './BWords.txt'
Words = []

class AutoMod(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        self.words = Words

# Need to rework auto deleted words
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 804150363602419782:
            pass
        else:
            Words = None
            with open(Wdir, 'r') as txt:
                Words = txt.read().strip().split(', ')
                print(Words)
                if any([word in message.content for word in Words]):
                    print(Words)
                    await message.delete()
                    await message.channel.send(f'{message.author.mention}, You are not allowed to say that.')
                else:
                    print('none')

    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, arg):
        Amount = int(arg)
        if arg:
            await ctx.channel.purge(limit=Amount)
        else:
            await ctx.send('You must add an amount of messages to clear (ex. db!clear 10).')
    @clear.error
    async def ClearError(self, ctx, arg):
        await ctx.send('Unable to clear messages. You proabably don\'t have permission to delete messages.')

    @commands.command()
    @has_permissions(manage_roles=True)
    async def mute(self, ctx, args):
        if len(args) < 1:
            await ctx.send('You didn\'t tell me who to mute!')
        if len(args) == 1:
            user = args[0]
            muted = discord.utils.get(ctx.guild.roles, name=str('muted'))
            await user.add_roles(muted)
            await ctx.send(f'{user} has been muted')
    @mute.error
    async def MuteError(self, ctx, args):
        await ctx.send('You do not have permission to do this. You must manage_roles permission.')

    @commands.command()
    @has_permissions(manage_messages=True)
    async def Warn(self, ctx, member: discord.Member):
        reason1 = ctx.message.content.replace('{}'.format(member), '')
        reason = reason1.replace('db!warn ', '')
        await member.send(f'Don\'t do that. (Warned by {ctx.message.author}).'+f' **Reason:** {reason}')
        embed=discord.Embed(title='Warned {}'.format(member), description=f'**Reason:** {reason}')
        embed.set_author(name=(ctx.message.author), icon_url=(ctx.message.author.avatar_url))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AutoMod(bot))
