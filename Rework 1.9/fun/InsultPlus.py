import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio
import random
from random import choice


class InsultPlus(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot

    Insults = [ #list of Insults for the insult command.
        'Ordinarily people live and learn. You just live.',
        'You\'re not funny, but your life, now that\' a joke.',
        'You\'re as useless as a computer without internet.',
        'YOUR ASININE SIMIAN COUNTENANCE ALLUDES THAT YOUR FETID STENCH HAS ANULLED THE ANTHROPOID APE SPECIES DIVERSITY',
        'You\'re not pretty enough to be this stupid.',
        'You\'re so stupid, it takes you an hour to cook Minute Rice.',
        'When you were born, they threw away the baby and kept the Placenta.',
        'Some day your frustrations with other people will end, but only because you will die alone.',
        'Everyone who ever loved you was wrong.',
        'I bet your brain feels good as new, seeing that you never use it.'
    ]

    Compliments = [ #list of comliments for the compliment command.
        'The FBI tapped your phone just to hear the sound of your voice.',
        'People behind you at the movies think you are the perfect height.',
        'There was a high school rumor that you are a distant relative of Abraham Lincoln.',
        'Callers are intimidated by how funny your voicemail greeting is.',
        '80% of motorcycle gangs think you\'d be a delightful sidecar.',
        'You are your parent\'s greatest accomplishment, unless they invented the \"spork\"',
        'You never forget to fill the ice-cube tray.',
        'Your allergies are some of the least embarrassing allergies.',
        'Some dudes hope you start a band so they can start a cover band of that band.',
        'Kids think you are the \"cool old person\".'
    ]

    @commands.command(name='Insult', brief='What do you think it does?')
    async def insult(self, ctx): #Insult command, picks an insult from the list of insults and sends it.
        choice = random.choice(Insults)
        await ctx.send(choice)
        print(f'Insulted {ctx.message.author}')

    @commands.command(name='Compliment', breif='A bunch of backhanded compliments.')
    async def compliment(self, ctx): #Complimentcommand, picks a compliment from the list of compliments and sends it.
        choice = random.choice(Insults)
        await ctx.send(choice)
        print(f'Complimented {ctx.message.author}')

def setup(bot):
    bot.add_cog(InsultPlus(bot))
