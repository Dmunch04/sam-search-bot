import discord

# Function that returns the current server
async def get_server (ctx):
    server = ctx.message.server

    return server

# Function that returns a servers name
async def get_server_name (server):
    server_name = server.name

    return server_name

# Function that returns all the servers members
async def get_server_members (server):
    server_members = server.members

    return server_members

# Function that returns the amount of members in the server
async def get_server_member_count (server):
    server_member_count = server.member_count

    return server_member_count

# Function that returns all the servers channels
async def get_server_channels (server):
    server_channels = server.channels

    return server_channels

# Function that returns all the servers roles
async def get_server_roles (server):
    server_roles = server.roles

    return server_roles

# Function that returns the owner of the server
async def get_server_owner (server):
    server_owner = server.owner

    return server_owner

# Function that returns all the servers emojis
async def get_server_emojis (server):
    server_emojis = server.emojis

    return server_emojis

# Function that returns the servers region
async def get_server_region (server):
    server_region = server.region

    return server_region

# Function that returns the servers icon
async def get_server_icon (server):
    server_icon = server.icon

    return server_icon

# Function that returns the servers id
async def get_server_id (server):
    server_id = server.id

    return server_id
