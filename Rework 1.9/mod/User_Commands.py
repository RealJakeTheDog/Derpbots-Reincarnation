import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio

class UserMod(commands.Cog, name='Moderator'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_roles=True)
    async def mute(self, ctx, args): #mute command, mutes a designated user.
        if len(args) < 1:
            user = args[0]
            muted = discord.utils.get(ctx.guild.roles, name=str('muted'))
            await user.add_roles(muted)
            embed = discord.Embed(title=(user.mention), color=discord.Color(16711680), description='Has been muted.')
            await ctx.send(embed=embed)
            await user.send(f'You have been muted in {ctx.guild}.')

    @commands.command()
    @has_permissions(manage_roles=True)
    async def unmute(self, ctx, args): #unmute command, unmutes a designated user.
        if len(args) < 1:
            user = args[0]
            muted = discord.utils.get(ctx.guild.roles, name=str('muted'))
            await user.remove_roles(muted)
            embed = discord.Embed(title=(user.mention), color=discord.Color(16711680), description='Has been unmuted')
            await ctx.send(embed=embed)
            await user.send(f'You have been unmuted in {ctx.guild}.')

    @commands.command()
    @has_permissions(manage_messages=True)
    async def Warn(self, ctx, member: discord.Member): #warn command, warns a designated user.
        reason1 = ctx.message.content.replace('{}'.format(member), '')
        reason = reason1.replace('db!warn ', '')
        await member.send(f'Don\'t do that. (Warned by {ctx.message.author}).'+f' **Reason:** {reason}')
        embed=discord.Embed(title='Warned {}'.format(member), description=f'**Reason:** {reason}')
        embed.set_author(name=(ctx.message.author), icon_url=(ctx.message.author.avatar_url))
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(UserMod(bot))
