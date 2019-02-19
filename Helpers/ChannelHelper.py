import discord
from Helper import ServerHelper as serverHelper

# Function for getting a channel by it's name
async def get_channel (server, channel_name):
    channel = discord.utils.get(server.get_all_channels(), server__name = server.name, name = channel_name)

    return channel

# Function that returns the default channel of the server
async def get_default_channel ():
    default_channel = server.default_channel()

    return default_channel

# Function that returns the name of the channel
async def get_channel_name (channel):
    channel_name = channel.name

    return channel_name

# Function that returns the channels topic/subject
async def get_channel_topic (channel):
    channel_topic = channel.topic

    return channel_topic

# Function that returns the channels type (Voice or Text)
async def get_channel_type (channel):
    channel_type = channel.type

    return channel_type

# Function that returns the channels id
async def get_channel_id (channel):
    channel_id = channel.id

    return channel_id

# Function that returns the server of the channel
async def get_channel_server (channel):
    channel_server = channel.server

    return channel_server

# Function that returns a bool whether the channel is private or not
async def get_channel_private (channel):
    channel_isprivate = channel.is_private

    return channel_isprivate

# Function that returns the channels postion in the channel hierarchy
async def get_channel_position (channel):
    channel_postion = channel.position

    return channel_postion

# Function that returns a bool whether the channel is default or not
async def get_channel_isdefault (channel):
    channel_isdefault = channel.is_default

    return channel_isdefault

# Function that returns the time the channel was created
async def get_channel_time_created (channel):
    channel_time_created = channel.created_at

    return channel_time_created
