import discord
from discord.ext import commands
from time import sleep
from discord.utils import get
from discord.ext.commands import Bot
import csv
import re
from discord.ext.commands import has_permissions

Words = []
Wdir = ('./BWords.txt')

class BlacklistedWords(commands.Cog):
    '''Automod Blacklisted Words'''
    def __init__ (self, bot):
        self.bot = bot
        self.words = Words

    @commands.Cog.listener()
    async def on_ready(self):
        self.words = {}
        with open(Wdir, 'r') as txt:
             Words = txt.read().strip().split(',')
        print(f'Blacklisted {Words}')

    @commands.command()
    @has_permissions(manage_messages=True)
    async def Blacklist(self, ctx, arg):
        with open(Wdir, 'w+') as txt:
            Words = txt.read().strip().split(', ')
            Words.append(arg)
            txt.write(Words)
        print(Words)
        print(f'Blacklisted word {arg}')
        await ctx.send(f'You have blacklisted the word {arg}. If you would like to undo this, run db!whitelist {arg}.')
    @Blacklist.error
    async def BlacklistError(self, ctx, arg):
        await ctx.send('You do not have permission to do this. You must have Manage_Messages permission.')

    @commands.command()
    @has_permissions(manage_messages=True)
    async def Whitelist(self, ctx, arg):
        try:
            with open(Wdir, 'w') as txt:
                Words = txt.read().strip().split(', ')
                if arg in Words:
                    for arg in Words:
                        Words.remove(arg)
                        await ctx.send(f'Whitelisted {arg}')
                else:
                    await ctx.send(f'{arg} is not a blacklisted word.')
        except:
            await ctx.send(f'Unable to whitelist {arg}. Please contact me.')

        else:
            await ctx.send(f'{arg} is not a blacklisted word. This command is used to un-blacklist commands from the automod.')
    @Whitelist.error
    async def WhitelistError(self, ctx, arg):
        await ctx.send('You do not have permission to do this. You must have Manage_Messages permission.')

def setup(bot):
    bot.add_cog(BlacklistedWords(bot))
