import discord
import asyncio
from discord.ext import commands

client = discord.Client()

@client.event
async def on_read():
    print("Connecté en tant que:",client.user.name)
    print("ID:",client.user.id)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content == "Bonjour":
        await client.send_message(message.channel, "Tout le monde")
        
client.run("NTU2NTM0ODUyMTM3MjU0OTMy.D3EYOg.3PZrCznNxFMg8dVwfLRuxigegQk")
