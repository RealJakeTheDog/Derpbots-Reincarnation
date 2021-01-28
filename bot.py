#Import
import discord
import random
from time import sleep

#Reset Variables
Insult = 0
Lottery = 0


#creating a new discord client
client=discord.Client()

#methods waiting for the event
@client.event

#Prints Username/User ID after starting
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(client.user.name)
    print("Userid: ",end='')
    print(client.user.id)
@client.event

#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#when the bot gets the message this method gets triggered
async def on_message(message):
    Insult = 0
    sleep(1)
    Insult = (random.randint(1,10))
    if message.author.id == client.user.id:
        return
    #test command
    if message.content.startswith('db!test'):
        await message.channel.send('This Command Is Useless'.format(message))
    #derpbot command
    elif message.content.startswith('db!derpbot'):
        await message.channel.send('I am the reincarnation of the once powerful Derpbot (Invite link: https://bit.ly/2YmxOfw)')
    #say command
    elif message.content.startswith('db!say'):
        await message.channel.send(message.content.replace('db!say ',''))
    #Despacito Command
    elif message.content.startswith('db!despacito'):
        await message.channel.send('```Despacito```' + '{0.author.mention}')
    #Help Command
    elif message.content.startswith('db!help'):
        await message.channel.send('''```
        db!test: A way to check if the bot is actually online
        db!derpbot: a small intro to the bot, including the invite link
        db!say [Text]: Makes the bot say something, replace [Text] with whatever you would like
        db!despacito: despacito
        db!help: ...
        db!insult: Take A Random Guess
        db!compliment: A bunch of backhanded compliments```''')
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
            await message.channel.send('Kids think you are the “cool old person”.')
  # Bot Token/Run
client.run("*************")
