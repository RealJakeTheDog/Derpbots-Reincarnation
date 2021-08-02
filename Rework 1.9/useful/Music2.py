import discord, youtube_dl, time, os, asyncio, ffmpeg, datetime
from discord.ext import commands
from async_timeout import timeout
from discord import FFmpegPCMAudio
from discord.utils import get
from discord import member

ydl_opts = {
    'format': 'bestaudio/best',
    'default_search': 'auto',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',

    }],
}

class MusicBeta(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.queue=asyncio.Queue(maxsize=0)
        self.song=''
    @commands.command()
    async def BPlay(self, ctx, url):
        if not ctx.message.author.voice:
            await ctx.send('You are not connected to a voice channel')
            return
        else:
            channel = ctx.message.author.voice.channel
            
        voice_client=await channel.connect()
        guild=ctx.message.guild
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            file=ydl.extract_info(url, download=True)
            path=str(file['title']) + '-' + str(file['id' + '.mp3'])
            await self.queue.put(path)
            await MusicBeta.start_playing(voice_client, ctx, guild)
    async def start_playing(self, voice_client, player, ctx, guild):
        def endSong(guild):
            os.remove(self.song)
        while True:
            async with timeout(5):
                try:
                    self.song=await self.queue.get()
                    print(self.song)
                except asyncio.TimeoutError:
                    print('Timeout Error')
                    break
            try:
                if self.song:
                    await voice_client.play(discord.FFmpegPCMAudio(self.song), after=lambda x: endSong(guild))
                if self.song == None:
                    await voice_client.disconnect()
            except:
                pass   

def setup(bot):
    bot.add_cog(MusicBeta(bot))