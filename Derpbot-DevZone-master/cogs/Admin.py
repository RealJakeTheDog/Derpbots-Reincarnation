import discord
from discord.ext import commands
from discord.ext.commands import Bot

initial_extensions = [
    'cogs.Useful',
    'cogs.Fun',
    'cogs.Music',
    'cogs.AutoMod-Blacklisted_Words',
    'cogs.AutoMod',
    'cogs.Config'
]

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner
    async def reload(self, ctx, arg):
        if arg:
            try:
                bot.reload_extension(arg)
                await ctx.send(f'Reloaded {arg}')
            except:
                await ctx.send(f'Was unable to reload {arg}, please try again.')
        else:
            for extension in initial_extensions:
                bot.reload_extension(extension)
    @reload.error
    async def reload_error(self, ctx, arg):
        await ctx.send('You do not have permission to do this.')

    @commands.command(hidden=True)
    @commands.is_owner
    async def load(self, ctx, arg):
        try:
            bot.load_extension(arg)
            await ctx.send(f'Loaded {arg}.')
        except:
            await ctx.send(f'Unable to load {arg}.')
    @load.error
        async def load_error(self, ctx, arg):
            await ctx.send(f'{arg} is not a valid extension or you do not have permission to do this.')

    @commands.command(hidden=True)
    @commands.is_owner
    async def unload(self, ctx, arg):
        id = str(ctx.author.id)
        if id == '395269984374489089':
            try:
                bot.unload_extension(arg)
                await ctx.send(f'Unloaded {arg}.')
            except:
                await ctx.send(f'Unable to unload {arg}.')
    @unload.error
        async def unload_error(self, ctx, arg):
            await ctx.send('You do not have permission to do this.')

    @commands.is_owner
    @commands.command()
    async def Close(ctx):
        await bot.logout()

def setup(bot):
    bot.add_cog(Admin(bot))
