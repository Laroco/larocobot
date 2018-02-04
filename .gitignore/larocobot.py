import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from random import *

Client = discord.Client()
client = commands.Bot(command_prefix = "/")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.upper().startswith('YOP'):
        userID = message.author.id
        await client.send_message(message.channel, "Yo <@%s> !" % (userID))
    if message.content.upper().startswith('BONJOUR'):
        userID = message.author.id
        await client.send_message(message.channel, "Yo <@%s> !" % (userID))

    #if message.content.startwith('/8ball'):
        #userID = message.author.id
        #await client.send_message(message.channel, "<*> <@%s>" * (8ball[randint(0,len(8ball))]) % (userID))


#8ball = ["Oui","Non","Peut-être","Surement pas","Tu peux toujours rêver","Absolument","C'est certain"]
client.run('MzgyOTI1MTYxMzM2Mjc0OTQ0.DPcyrA.QjaETfilsi9Rlo-tcmQxRTXMOC0')


