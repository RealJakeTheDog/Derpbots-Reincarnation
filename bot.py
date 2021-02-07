#Import
import discord
import random
import asyncio
import discord.ext
import discord.voice_client
from discord.ext import commands
from discord.ext.commands import bot
from time import sleep
from discord import FFmpegPCMAudio
from discord.utils import get
from random import choice

#Reset Variables
Insult = 0
Counter = '0'
members = "test"
yesNo = 0
timer = 0


#creating a new discord client
intents = discord.Intents.all()
client=discord.Client(intents=intents)
bot = commands.Bot(command_prefix='db!')

#methods waiting for the event
@client.event

#Prints Username/User ID after starting
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(client.user.name)
    print("Userid: ",end='')
    print(client.user.id)
    await client.change_presence(status=discord.Status.online, activity=discord.Game("db!help"))
@client.event

#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#when the bot gets the message this method gets triggered
async def on_message(message):
    Insult = 0
    coin = 0
    Choice = 0
    sleep(0.3)
    Insult = (random.randint(1,10))
    coin = (random.randint(1,3))
    if message.author.id == client.user.id:
        return
    #test command
    if message.content.startswith('db!test'):
        await message.channel.send('Hello '+ (message.author.mention))
    #derpbot command
    elif message.content.startswith('db!derpbot'):
        await message.channel.send('I am the reincarnation of the once powerful Derpbot (Invite link: https://bit.ly/2YmxOfw)')
    #say command
    elif message.content.startswith('db!say'):
        await message.channel.send(message.content.replace('db!say ',''))
    #Despacito Command
    elif message.content.startswith('db!despacito'):
        await message.channel.send('Did some carbon based life form just say \*\*\*DESPACITO\*\*\*')
    #Help Command
    elif message.content.startswith('db!help'):
        await message.channel.send('''```
        db!test: A way to check if the bot is actually online
        db!derpbot: a small intro to the bot, including the invite link
        db!say [Text]: Makes the bot say something, replace [Text] with whatever you would like
        db!despacito: Despacito
        db!help: ...
        db!insult: Take A Random Guess
        db!compliment: A bunch of backhanded compliments
        db!FlipACoin: Flips A Coin
        db!doing: Changes the bot's status
        db!deleteserver: Power Manifested
        db!roulette: Pings a random User
        db!colors: Lists The Colors Available
        db!Color: Sets Your Color (RUN db!Color Clear FIRST)```''')
    #Insult Command
    if message.content.startswith('db!insult'):
        if Insult == 1 :
            await message.channel.send('ORDINARILY PEOPLE LIVE AND LEARN. YOU JUST LIVE.')
        elif Insult == 2 :
            await message.channel.send('YOU\'RE NOT FUNNY, BUT YOUR LIFE, NOW THAT\'S A JOKE.')
        elif Insult == 3 :
            await message.channel.send('YOU\'RE AS USELESS AS A COMPUTER WITHOUT INTERNET.')
        elif Insult == 4 :
            await message.channel.send('YOUR ASININE SIMIAN COUNTENANCE ALLUDES THAT YOUR FETID STENCH HAS ANULLED THE ANTHROPOID APE SPECIES DIVERSITY.')
        elif Insult == 5 :
            await message.channel.send('YOU\'RE NOT PRETTY ENOUGH TO BE THIS STUPID.')
        elif Insult == 6 :
            await message.channel.send('YOU\'RE SO STUPID, IT TAKES YOU AN HOUR TO COOK MINUTE RICE.')
        elif Insult == 7 :
            await message.channel.send('WHEN YOU WERE BORN, THEY THREW AWAY THE BABY AND KEPT THE PLACENTA...')
        elif Insult == 8 :
            await message.channel.send('SOMEDAY YOUR FRUSTRATIONS WITH OTHER PEOPLE WILL END, BUT ONLY BECAUSE YOU WILL DIE ALONE.')
        elif Insult == 9 :
            await message.channel.send('EVERYONE WHO EVER LOVED YOU WAS WRONG')
        elif Insult == 10 :
            await message.channel.send('I BET YOUR BRAIN FEELS AS GOOD AS NEW, SEEING THAT YOU NEVER USE IT.')
    #Compliment Command
    if message.content.startswith('db!compliment'):
        if Insult == 1 :
            await message.channel.send('The FBI tapped your phone just to hear the sound of your voice.')
        if Insult == 2 :
            await message.channel.send('People behind you at movies think you are the perfect height.')
        if Insult == 3 :
            await message.channel.send('There was a high school rumor that you are a distant relative of Abraham Lincoln.')
        if Insult == 4 :
            await message.channel.send('Callers are intimidated by how funny your voicemail greeting is.')
        if Insult == 5 :
            await message.channel.send('80% of motorcycle gangs think you’d be a delightful sidecar.')
        if Insult == 6 :
            await message.channel.send('You are your parent\'s greatest accomplishment, unless they invented the \"spork\".')
        if Insult == 7 :
            await message.channel.send('You never forget to fill the ice-cube tray.')
        if Insult == 8 :
            await message.channel.send('Your allergies are some of the least embarrassing allergies.')
        if Insult == 9 :
            await message.channel.send('Some dudes hope you start a band so they can start a cover band of that band.')
        if Insult == 10 :
            await message.channel.send('Kids think you are the \“cool old person\”.')
    if message.content.startswith('db!FlipACoin'):
        if coin == 1 :
            await message.channel.send('It Was Heads')
        if coin == 2 :
            await message.channel.send('It Was Tails')
        elif coin == 3 :
            await message.channel.send('The Coin Landed On Its Side')
    if message.content.startswith('GG!EnD01230'):
        await message.channel.send('Goodbye')
        await client.change_presence(status=discord.Status.invisible)
        sleep(1)
        await client.close()
    if message.content.startswith('db!doing'):
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message.content.replace('db!doing','')))
        await message.channel.send("Doing ur mom")
    if message.content.startswith('db!deleteserver'):
        print ('A Random Sever Has Been Deleted')
        await message.channel.send(message.author.mention + " Has Deleted A Random Server")
        await message.channel.send('I have used my power to delete a server. What server? I have no clue.')
    if message.content.startswith('db!roulette'):
        print(message.channel.members)
        user = random.choice(message.channel.members)
        await message.channel.send(': %s is dead' % user.mention)
    if message.content.startswith('db!colors'):
        await message.channel.send('''
        &
        ```Please Run db!Color Clear to clear your colors before selecting a new color.```
        >>> Available Colors:
        Lime
        Yellow
        Aqua
        Blue
        Bright Orange
        Light Green
        Black
        Navy
        Salmon
        Pink
        Dark Red
        Brown
        Purple''')
    if message.content.startswith('db!Color'):
        user = message.author
        print(user)
        color = message.content.replace('db!Color ','')
        print(color)
        sleep(0.3)
        if color == 'Lime':
            role = get(user.guild.roles, name = 'Lime')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Lime Role')
        elif color == 'Yellow':
            role = get(user.guild.roles, name = 'Yellow')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Yellow Role')
        elif color == "Aqua":
            role = get(user.guild.roles, name = 'Aqua')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Aqua Role')
        elif color == "Blue":
            role = get(user.guild.roles, name = 'Blue')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Blue Role')
        elif color == "Bright Orange":
            role = get(user.guild.roles, name = 'Bright Orange')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Bright Orange Role')
        elif color == "Light Green":
            role = get(user.guild.roles, name = 'Light Green')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Light Green Role')
        elif color == "Black":
            role = get(user.guild.roles, name = 'Black')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Black Role')
        elif color == "Navy":
            role = get(user.guild.roles, name = 'Navy')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Navy Role')
        elif color == "Salmon":
            role = get(user.guild.roles, name = 'Salmon')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Salmon Role')
        elif color == "Pink":
            role = get(user.guild.roles, name = 'Pink')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Pink Role')
        elif color == "Dark Red":
            role = get(user.guild.roles, name = 'Dark Red')
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Dark Red Role')
        elif color == "Brown":
            role = get(user.guild.roles, name = "Brown")
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Brown Role')
        elif color == "Purple":
            role = get(user.guild.roles, name = "Purple")
            await user.add_roles(role)
            await message.channel.send('Gave '+ (message.author.mention) + ' Purple Role')
        elif color == "Clear":
            removeColors = ('Lime', 'Yellow', 'Aqua', 'Blue', 'Bright Orange', 'Light Green', 'Black', 'Navy', 'Salmon', 'Pink', 'Dark Red', 'Brown', 'Purple')
            role = tuple(get(user.guild.roles, name = n)for n in removeColors)
            await user.remove_roles(*role)
            print('Reset Colors')
            await message.channel.send('Reset Color')
#______________________________________________________________________________________________________________________________________________________________________________
  # Bot Token/Run
client.run("*************")
