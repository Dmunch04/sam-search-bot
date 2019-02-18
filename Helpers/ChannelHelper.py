import discord
from Helper import ServerHelper as serverHelper

# Function for getting a channel by it's name
async def get_channel (channel_name):
    server = serverHelper.get_server()
    print("Get channel")

#https://discordpy.readthedocs.io/en/latest/api.html#discord.Channel
