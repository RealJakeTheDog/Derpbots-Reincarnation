import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio
import sys
import traceback

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        cog=ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        ignored=(commands.CommandNotFound, asyncio.exceptions.TimeoutError, asyncio.exceptions.CancelledError) #Ingores if there is no command available
        error = getattr(error, 'original', error)
        if isinstance(error, ignored):
            return
        if isinstance(error, commands.DisabledCommand): #Checks if the command has been disabled
            await ctx.send(f'{ctx.command} has been disabled.')
        elif isinstance(error, commands.NoPrivateMessage): #Checks if the command was used in a DM when it wasn't allowed to be
            try:
                await ctx.author.send(f'{ctx.command} cannot be used in Private Messages.')
            except discord.HTTPException:
                pass
        elif isinstance(error, commands.BadArgument): #Checks if Arguments are missing
            if ctx.command.qualified_name== 'tag list':
                await ctx.send('I could not find that member. Please try again.')
        elif isinstance(error, commands.MissingPermissions): #Checks if user is missing permissions
                await ctx.send('You don\'t have permissions to do that!')
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send('This command is currently on cooldown!')
        else: #If error is none of the above
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            await ctx.send(f'```Unable to find reason for error. Original Error: {error}```')

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
