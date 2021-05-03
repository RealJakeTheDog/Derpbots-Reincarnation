import discord
from discord.ext import commands
from discord.ext.commands import Bot

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True) #Load Cog Command
    async def load(self, ctx, arg):
        self.bot.load_extension(arg)
        await ctx.send('loaded')
    @commands.command(hidden=True) #Unload Cog Command
    async def unload(self, ctx, arg):
        self.bot.unload_extension(arg)
        await ctx.send('unloaded')
    @commands.command(hidden=True) #Reload Cog Command
    async def reload(self, ctx, arg):
        self.bot.reload_extension(arg)
        await ctx.send('reloaded')


def setup(bot):
    bot.add_cog(Admin(bot))
