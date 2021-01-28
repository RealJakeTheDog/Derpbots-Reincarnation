#importing the discord module
import discord

#creating a new discord client
client=discord.Client()

#methods waiting for the event
@client.event

#when the bot started running, we may print its name, id etc
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(client.user.name)
    print("Userid: ",end='')
    print(client.user.id)
@client.event

#when the bot gets the message this method gets triggered
async def on_message(message):
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
        db!help: ...```''')

# Bot Token/Run
client.run("ODA0MDM2MTAzNDA5MzY5MDk4.YBGe-Q.CxUgdR4lOfp7os_aVlzFZB3Erhc")
# Main Bot Token: ODA0MDM2MTAzNDA5MzY5MDk4.YBGe-Q.CxUgdR4lOfp7os_aVlzFZB3Erhc
# Edge Bot Token: ODA0MTUwMzYzNjAyNDE5Nzgy.YBIJYw.LIJrEBtPKgqTP1IwSEsH4bgYt5s
