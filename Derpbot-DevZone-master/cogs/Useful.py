import discord
import asyncio
from discord.ext import commands
from time import sleep
from discord.utils import get
from discord.ext.commands import Bot, has_permissions, CheckFailure

class Useful(commands.Cog):
    '''Useful Commands Like Color and Status'''

    def __init__(self, bot):
        self.bot = bot

# db!test command
    @commands.command(brief ='A way to check if the bot is actually online')
    async def test(self, ctx):
        await ctx.send('Hello ' + (ctx.author.mention))


# db!derpbot command
    @commands.command(brief = 'A small intro to the bot, including the invite link')
    async def derpbot(self, ctx):
        await ctx.send('I am the reincarnation of the once powerful Derpbot (Invite link: https://bit.ly/2YmxOfw) ')


# db!color command
# Creates a role named the username of whoever called the command, colors it, and then gives it to them.
# End Goal - Be able to move the roles higher so that they do not interfere with other role colors and allows you to actually have other colored roles - If you know how feel free to tell me in the discussions tab!
    @commands.command(brief = 'Changes Your Color Using db!color (HEX CODE), use db!help color for more information.', description ='''Use db!color (HEX CODE) to set your own Color!
    You can find custom Hex Codes at:
    PC: __https://bit.ly/2ZWfOJF__
    Mobile: __https://bit.ly/3bMcKFw__''' )
    async def color(self, ctx, arg):
        role = ctx.author
        color = (arg)
        guild = ctx.author.guild
        user = ctx.author
        ze = discord.utils.get(ctx.guild.roles, name=str(role))
        await asyncio.sleep(0.3)
        print(color)
        print(role)
        print(ze)
        if get(ctx.guild.roles, name=str(role)):
            await ze.edit(color=int(color, 16))
            await asyncio.sleep(0.2)
            await user.add_roles(ze)
        else:
            await guild.create_role(name=str(role), color=int(color, 16))
            await asyncio.sleep(0.2)
            await user.add_roles(ze)

def setup(bot):
    bot.add_cog(Useful(bot))
