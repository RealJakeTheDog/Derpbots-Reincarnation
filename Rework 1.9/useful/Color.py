import discord
import asyncio
from discord.ext import commands
from time import sleep
from discord.utils import get
from discord.ext.commands import Bot, has_permissions, CheckFailure

class Color(commands.Cog, name='Useful'):
    '''Useful Commands Like Color and Status'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = 'Changes Your Color Using db!color (HEX CODE), use db!help color for more information.', description ='''Use db!color (HEX CODE) to set your own Color!
    You can find custom Hex Codes at:
    PC: __https://bit.ly/2ZWfOJF__
    Mobile: __https://bit.ly/3bMcKFw__''' )
    async def color(self, ctx, arg): #color command, makes a role named that user (if not already made) and set's the color designated. Then gives the role to the user.
        color = (arg)
        guild = ctx.author.guild
        user = ctx.author
        ze = discord.utils.get(ctx.guild.roles, name=str(user))
        if get(ctx.guild.roles, name=str(user)):
            await ze.edit(color=int(color, 16))
            await user.add_roles(ze)
        else:
            await guild.create_role(name=str(user), color=int(color, 16))
            await user.add_roles(ze)

def setup(bot):
    bot.add_cog(Color(bot))
