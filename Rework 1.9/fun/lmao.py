import discord
from discord.ext import commands
from discord import Emoji

class Lmao(commands.Cog, name='Funny'):
    def __init__(self, bot):
        self.bot=bot
    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.bot.get_channel(id=442514633908158464)
        if message.channel == channel:
            print('1')
            guild = message.channel.guild
            print(guild)
            lemon = guild.get_member(314492807580745728)
            vivian= guild.get_member(616964861582376960)
            if message.author == lemon:
                print('2')
                await message.channel.send('<:Lmao:849750180756193331>')
            if message.author == vivian:
                print('2')
                await message.channel.send('<:Lmao:849750180756193331>')
            #if message.author == evan:
                #print('2')
                #await message.channel.send('<:Lmao:849750180756193331>')
            else:
                pass
        else:
            print('3')
def setup(bot):
    bot.add_cog(Lmao(bot))