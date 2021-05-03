import discord
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio

class TextMod(commands.Cog, name='Moderator'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, arg): #clear command, clears a designated amount of messages.
        Amount = int(arg)
        user = ctx.message.author
        if arg:
            await ctx.channel.purge(limit=Amount)
            await user.send(f'Cleared {Amount} message(s).')
        else:
            await ctx.send('You must add an amount of messages to delete')
    @clear.error
    async def ClearError(self, ctx, arg):
        await ctx.send('Unable to clear messages. You probably don\'t have permission to delete messages.')

def setup(bot):
    bot.add_cog(TextMod(bot))
