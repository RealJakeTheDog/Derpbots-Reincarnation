import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import Bot

class Fun(commands.Cog):
    '''Fun Commands That Don't Do Much'''
    def __init__(self, bot):
        self.bot = bot

#db!say command
    @commands.command(brief='Makes the bot say something')
    async def say(ctx, *, arg):
            await ctx.send(arg)
            sleep(1)

#db!despacito command
    @commands.command(brief='Despacito')
    async def despacito(ctx):
        await ctx.send('Did some carbon based life form just say ***DESPACITO***')

#db!insult command - Looking for a better/more efficient way of doing this command. If you have any ideas let me know in the discussions tab.
    @commands.command(brief='For Masochists')
    async def insult(ctx):
        Insult = 0
        sleep(0.5)
        Insult = (random.randint(1,10))
        sleep(0.2)
        if Insult == 1:
            await ctx.send('Ordinarily people live and learn. You just live.')
        if Insult == 2:
            await ctx.send('You\'re not funny, but your life, now that\' a joke.')
        if Insult == 3:
            await ctx.send('You\'re as useless as a computer without internet.')
        if Insult == 4:
            await ctx.send('YOUR ASININE SIMIAN COUNTENANCE ALLUDES THAT YOUR FETID STENCH HAS ANULLED THE ANTHROPOID APE SPECIES DIVERSITY')
        if Insult == 5:
            await ctx.send('You\'re not pretty enough to be this stupid.')
        if Insult == 6:
            await ctx.send('You\'re so stupid, it takes you an hour to cook Minute Rice.')
        if Insult == 7:
            await ctx.send('When you were born, they threw away the baby and kept the Placenta.')
        if Insult == 8:
            await ctx.send('Some day your frustrations with other people will end, but only because you will die alone.')
        if Insult == 9:
            await ctx.send('Everyone who ever loved you was wrong.')
        if Insult == 10:
            await ctx.send('I bet your brain feels good as new, seeing that you never use it.')

    @commands.command(brief='A bunch of backhanded compliments')
    async def compliment(ctx):
        Compliment = 0
        sleep (0.5)
        Compliment = (random.randint(1,10))
        sleep(0.2)
        if Compliment == 1:
            await ctx.send('The FBI tapped your phone just to hear the sound of your voice.')
        if Compliment == 2:
            await ctx.send('People behind you at the movies think you are the perfect height.')
        if Compliment == 3:
            await ctx.send('There was a high school rumor that you are a distant relative of Abraham Lincoln.')
        if Compliment == 4:
            await ctx.send('Callers are intimidated by how funny your voicemail greeting is.')
        if Compliment == 5:
            await ctx.send('80% of motorcycle gangs think you\'d be a delightful sidecar.')
        if Compliment == 6:
            await ctx.send('You are your parent\'s greatest accomplishment, unless they invented the \"spork\"')
        if Compliment == 7:
            await ctx.send('You never forget to fill the ice-cube tray.')
        if Compliment == 8:
            await ctx.send('Your allergies are some of the least embarrassing allergies.')
        if Compliment == 9:
            await ctx.send('Some dudes hope you start a band so they can start a cover band of that band.')
        if Compliment == 10:
            await ctx.send('Kids think you are the \"cool old person\".')

    @commands.command(brief='Flips a coin')
    async def FlipACoin(ctx):
        coin = 0
        sleep(0.5)
        coin = random.randint(1,2)
        sleep(0.2)
        if coin == 1:
            await ctx.send(':coin: It was heads.')
        if coin == 2:
            await ctx.send(':coin: It was tails.')

    @commands.command(brief='Power Manifested')
    async def deleteserver(ctx):
        print ('db!deleteserver')
        await ctx.send(ctx.author.mention + ' Has Deleted A Random Server')
        await ctx.send('I have used my power to delete a server. What server? I have no clue.')







def setup(bot):
    bot.add_cog(Fun(bot))
