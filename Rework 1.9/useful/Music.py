import discord
from discord import Embed
import os
import asyncio
import youtube_dl
import ffmpeg
import datetime
from time import sleep
import urllib.parse, urllib.request, re
import requests
from discord.ext import commands
from discord import Embed, FFmpegPCMAudio
from discord.utils import get
from discord import member

queue = []


# Options for YTDL. DO NOT TOUCH POST PROCESSORS. IT WILL NOT WORK IF THOSE SETTINGS ARE CHANGED.
ydl_opts = {
    'format': 'bestaudio/best',
    'default_search': 'auto',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',

    }],
}

# Options for ffmpeg. This isn't really used so changing options won't do much.
ffmpeg_options = {
    'options': '-vn'
}

# Sets YTDL options.
ytdl = youtube_dl.YoutubeDL(ydl_opts)


# Gives Metadata for YTDL. Use data.get() to download more Metadata about the URL that was sent. Use the volume variable to set default volume for the bot.
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.15):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.author = data.get('uploader')
        self.thumbnail = data.get('thumbnail_url')
        self.url = data.get('url')
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False, play=False):
        loop=loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream or play))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.queue=queue

# db!play command
    @commands.command(
        name = 'play',
        aliases =['p'],
        brief = 'Plays a song using a link or search',
        description = 'Plays a song using a link or search. Use db!play (Link) for a better experience.'
    )
    async def play(self, ctx, *, url):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            print('Already in channel')
        else:
            await self.join(ctx)
            await asyncio.sleep(0.3)
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            if len(self.queue) <= 0:
                self.queue[len(self.queue)] = player
                self.start_playing(ctx.voice_client, player, ctx)
                embed = discord.Embed(title=('***Now Playing***                                                                                         ' +'{}'.format(player.title) + 'by  {}'.format(player.author)), color=discord.Color(16711680), description = f'Searched for: {url}', timestamp=datetime.datetime.utcfromtimestamp(1615535295))
                embed.set_author(name=(ctx.author), icon_url=(ctx.author.avatar_url))
                embed.set_thumbnail(url= 'https://bit.ly/3cnA1xR')
                embed.set_footer(text='Derpbot Music',icon_url='https://bit.ly/3cnA1xR')

                await ctx.send(f':mag_right: **Searching for** ``' + url + '``')
                await ctx.send(embed=embed)
            else:
                queue.append(url)
                self.queue[len(self.queue)] = player
                embed = discord.Embed(title=('***Added To Queue***                                                                               ' +'{}'.format(player.title) + 'by {}'.format(player.author)), color=discord.Color(16711680), description = f'Searched for: {url}', timestamp=datetime.datetime.utcfromtimestamp(1615535295))
                embed.set_author(name=(ctx.author), icon_url=(ctx.author.avatar_url))
                embed.set_thumbnail(url= 'https://bit.ly/3cnA1xR')
                embed.set_footer(text='Derpbot Music',icon_url='https://bit.ly/3cnA1xR')
                await ctx.send(f':mag_right: **Searching for** ``' + url + '``')
                await ctx.send(embed=embed)
# This allows the next song in the queue to play. If you want to play a song with another command, use this and not self.play .
    def start_playing(self, voice_client, player, ctx):
        self.queue[0] = player
        i = 0
        sleep(0.2)
        while i <  len(self.queue):
            try:
                voice_client.play(self.queue[i], lambda _=None: {
                    self.start_playing(ctx.voice_client, player, ctx)
                })
            except:
                pass
            i += 1

    @commands.command(
        name='now_playing',
        brief='Shows what it currently playing',
        aliases=['playing'],
    )
    async def now_playing(self, ctx):
        player = await YTDLSource.from_url(queue[0], loop=self.bot.loop, stream=True)
        embed=discord.Embed(name=('***Now Playing***:  {}'.format(player.title)))
        await ctx.send(embed=embed)

#db!pause command
    @commands.command(brief = 'Pauses the music playing')
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice.pause()
        await ctx.send(f'Bot was paused by'+ ctx.message.author.mention)

#db!resume command
    @commands.command(
        name = 'resume',
        brief = 'Resumes the music playing'
    )
    async def resume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice.resume()
        await ctx.send(f'Bot was resumed by'+ ctx.message.author.mention)

#db!remove_queue command
    @commands.command(
        name = 'remove_queue',
        aliases=['remove'],
        brief = 'Removes a song from the queue',
        description = 'Use db!remove (Number) to remove a certain song from the queue'
    )
    async def remove_queue(self, ctx, number):
        global queue
        try:
            del(queue[int(number)+1])
            if len(queue)< 1:
                await ctx.send('Your queue is empty!')
            else:
                await ctx.send(f'Your queue is now {queue}')
        except:
            await ctx.send('List index out of range - the queue starts at 1')

#db!Clear Queue command
    @commands.command(
        name = 'clear_queue',
        aliases = ['ClearQueue'],
        brief = 'Removes all songs from the queue'
    )
    async def clear_queue(self, ctx):
        global queue
        queue.clear()
        await ctx.send(f'The queue was cleared by' + ctx.message.author.mention)

#db!queue command
    @commands.command(
        name = 'queue',
        aliases = ['q'],
        brief = 'Views the next song in the queue'
    )
    async def queue(self, ctx):
        if len(queue) < 1:
                await ctx.send('The queue is empty - add a song using db!play')
        else:
            await ctx.send('Grabbing Queue... (this may take a while)')
            Place = 0
            player = await YTDLSource.from_url(queue[0], loop=self.bot.loop, stream=False)
            embed = discord.Embed(title=('Queue:'), color=discord.Color(16711680), description=('Next:  {}'.format(player.title)))
            try:
                for url in queue:
                    Place += 1
                    print(Place)
                    player = await YTDLSource.from_url(queue[int(Place)], loop=self.bot.loop, stream=False)
                    embed.add_field(name=(f'Position {Place + 1}:'), value=('{}'.format(player.title)), inline=False)
            except:
                print('QueueError')
            await ctx.send(embed=embed)


#db!leave command
    @commands.command(
        name='leave',
        aliases=['l'],
        brief='Makes the bot leave the current channel'
    )
    async def leave(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        channel = ctx.message.author.voice.channel
        await voice.disconnect()
        await ctx.send(f'Disconnected from {channel}')

#db!add command
    @commands.command(
        name ='add',
        brief = 'Used as a troubleshooter',
        description='Use db!add (song, search) to add songs to the queue. db!play does this by default.',
        hidden=True
    )
    async def add(self, ctx, url):
        global queue
        try:
            queue.append(url)
            await ctx.send(f'{url} was added to the queue by '+ ctx.message.author.mention)
        except:
            await ctx.send(f'Couldn\'t add {url} to the queue - please try again' )

#db!join command
    @commands.command(
        name = 'join',
        aliases =['j'],
        brief = 'Makes the bot join your current voice channel'
    )
    @play.before_invoke
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send('You are not connected to a voice channel!')
            return
        else:
            channel = ctx.message.author.voice.channel
            self.queue = {}
            voice = get(self.bot.voice_clients, guild=ctx.guild)
            print(voice)
            if voice and voice.is_connected():
                await voice.move_to(channel)
                await ctx.send(f'Moved to {channel}')
            else:
                await channel.connect()
                await ctx.send(f'Connected to {channel}')

#db!skip command
    @commands.command(
        name = 'skip',
        aliases =['s'],
        brief = 'Skips current song'
    )
    async def skip(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        await ctx.send('Skipped Song')
        voice.stop()
        await self.start_playing

#db!PlayQueue command
    @commands.command(
        name = 'PlayQueue',
        brief = 'Used only as a troubleshooter',
        description = 'Use db!PlayQueue to play songs in the queue. db!play does this by default.',
        hidden=True
    )
    async def PlayQueue(self, ctx):
        if player.is_playing():
            pass
        for url in queue:
            try:
                async with ctx.typing():
                    player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                    ctx.voice_client.play(player, after=lambda e: print(f'Has Finished Playing'))
                await ctx.send(':white_check_mark:'+' **Now Playing:** ``{}'.format(player.title) + "``")
            except:
                await ctx.send('Unable to play queue - Please try again')


def setup(bot):
    bot.add_cog(Music(bot))
