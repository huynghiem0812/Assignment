import discord
import requests
import asyncio

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send("Hello!")

    if message.content.startswith('!cat'):
        while True:
            api_key = 'live_5uWKXutCelhVjS06DAWp2HiGLaXmtDf5Qxf5T4ph322fagAuhSZtMSIhTbK542B8'
            response = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={api_key}')
            data = response.json()[0]
            url = data['url']
            await message.channel.send(url)
            await asyncio.sleep(10)

client.run('DISCORD_TOKEN')
