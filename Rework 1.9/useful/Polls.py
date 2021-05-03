import discord
from discord.ext import commands
from discord.ext.commands import bot, has_permissions, CheckFailure
import asyncio
from discord.utils import get

class Polls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Test')
    async def CreatePoll(self, ctx, *args): #Poll command, makes a poll with Yes/No and lasts a designated amount of time.
        print('test')
        if len(args) == 3:
            user = ctx.message.author
            print(user)
            Poll = args[0]
            print(Poll)
            Channel = self.bot.get_channel(int(args[1]))
            embed = discord.Embed(title='New Poll', description=(Poll))
            embed.add_field(name='How To Vote:', value='Please react with :white_check_mark: for yes or :negative_squared_cross_mark: for no')
            embed.set_author(name=(user), icon_url=(user.avatar_url))
            embed.set_footer(text='Derpbot Polls')
            message = await Channel.send(embed=embed)
            await message.add_reaction('\U00002705')
            await message.add_reaction('\U0000274e')
            await asyncio.sleep(int(args[2]))
            Poll = args[0]
            print(Poll)
            message = await Channel.fetch_message(message.id)
            yes = get(message.reactions, emoji='\U00002705')
            no = get(message.reactions, emoji='\U0000274e')
            print(Poll)
            if yes.count > no.count:
                Poll = args[0]
                embed = discord.Embed(title=(Poll), description='The Answer is: `YES`')
                await message.edit(embed=embed)
            if yes.count < no.count:
                Poll = args[0]
                embed = discord.Embed(title=(Poll), description='The Answer is: `NO`')
                await message.edit(embed=embed)
            if yes.count == no.count:
                Poll = args[0]
                embed = discord.Embed(Title=(Poll), description='It Was A Tie!')
        elif len(args) < 3:
            user = ctx.message.author
            print(user)
            await user.send('''You did not add the poll you would like to send or the channel to send the poll in.
            `Format for creating Polls:`
            db!CreatePoll ("Poll") (Channel ID to Send Poll In) (Time limit of poll in seconds)
            If you do not know how to grab the channel id, please do db!ID''')

def setup(bot):
    bot.add_cog(Polls(bot))
