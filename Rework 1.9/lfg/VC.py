import discord
from discord.ext import commands
from discord.ext.commands import bot, has_permissions, CheckFailure, cooldowns
from discord.ext.commands.cooldowns import BucketType
import asyncio


class voice_channel(commands.Cog, name='LFG'):
    def __init__(self, ctx):
        self.bot = bot

    @commands.command(brief='Sends an Invite to join your VC.', description='Use db!lfg [User Limit] [Description] to invite people to join your VC. Description also sets your VC name so make it short.')
    @commands.cooldown(1, 180, commands.BucketType.guild)
    async def lfg(self, ctx, *, arg): #LFG Command, Invites people to join your voice channel.
        user = ctx.message.author
        vc = user.voice.channel
        ID = vc.name.split(None)
        inv = await vc.create_invite(temporary=True, reason='LFG Invite', max_age=3600)
        message = await ctx.send( f'Join {user.mention} in {ID[0]} '+ str(inv) + f'''
        ```{arg}```''')
        await vc.edit(name=(ID[0] + ' ' +str(arg)), reason = 'LFG')
        await asyncio.sleep(3600)
        await message.delete()

    @commands.command(brief='Changed your current voice channel\'s name')
    @commands.cooldown(1, 180, commands.BucketType.guild)
    async def set(self, ctx, *, arg): #set command, Set's your voice channel name + VC ID.
        user = ctx.message.author
        vc = user.voice.channel
        ID = vc.name.split(None)
        print(ID)
        await vc.edit(name=(ID[0] + ' ' + str(arg)), reason='LFG')
        message = await ctx.send(f'Changed Voice Channel name to {str(arg)}')
        await message.delete(delay=4)

    #@commands.command(brief='Sets the user limit in a Voice Channel.') NOT WORKING
    #@commands.cooldown(1, 900, commands.BucketType.guild)
    async def limit(self, ctx, limit): #limit command, Set's your voice channel limit.
        user = ctx.message.author
        vc = user.voice.channel
        await vc.edit(limit=int(limit))
        message = await ctx.send(f'Channel limit is now {limit}.')
        await message.delete(delay=4)

    @commands.command(name='Invite', short='Sends you a temporary invite to allow people to join your Voice Channel.')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def Invite(self, ctx): #Invite command, sends you a temporary invite to your voice channel.
        user = ctx.message.author
        VC = user.voice.channel
        if VC is None:
            await user.send('You must be in a Voice Channel to use this command.')
        else:
            inv = await VC.create_invite(temporary=True, reason='LFG Invite', max_age=3600)
            await user.send(f'''`Here is your invite:`
            {inv}''')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after): #Resets the Voice Channel to its ID once it's empty
        if before.channel:
            await asyncio.sleep(1)
            vc = member.guild.get_channel(before.channel.id)
            if not vc.members:
                print('Channel is empty')
                ID = vc.name.split(None)
                print(ID[0])
                await vc.edit(name=(ID[0]), limit=None, reason = 'Channel is empty')
                print(f'Channel renamed to {ID[0]}')
            else:
                print('There are still users in this channel.')
        else:
            pass

def setup(bot):
    bot.add_cog(voice_channel(bot))
