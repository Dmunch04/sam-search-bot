import discord

# Function that returns the name of a user
async def get_user_name (user : discord.Member):
    user_name = user.name

    return user_name

# Function that returns the users tag (#0000)
async def get_user_tag (user : discord.Member):
    user_tag = user.discriminator

    return user_tag

# Function that returns the users nickname in the server
async def get_user_nickname (user : discord.Member):
    user_nickname = user.display_name

    return user_nickname

# Function that returns the status of the user
async def get_user_status (user : discord.Member):
    user_status = user.status

    return user_status

# Function that returns the users avatar
async def get_user_avatar (user : disord.Member):
    user_avatar = user.avatar

    return user_avatar

# Function that returns the link to the users avatar
async def get_user_avatar_url (user : discord.Member):
    user_avatar_url = user.avatar_url

    return user_avatar_url

# Function that returns all the users roles
async def get_user_roles (user : discord.Member):
    user_roles = user.roles

    return user_roles

# Function that returns the users highest role (According to the servers role hierarchy)
async def get_user_top_role (user : discord.Member):
    user_top_role = user.top_role

    return user_top_role

# Function that returns the users color on the users side panel
async def get_user_color (user : discord.Member):
    user_color = user.color

    return user_color

# Functin that returns the users permissions in the given channel
async def get_user_channel_permission (user : discord.Member, channel):
    user_channel_permission = user.permissions_in(channel)

    return user_channel_permission

# Function that returns the users permissions in the current server
async def get_user_server_permissions (user : discord.Member):
    user_server_permissions = user.server_permissions

    return user_server_permissions

# Function that returns a bool whether the user is a bot or not
async def get_user_type (user : discord.Member):
    user_type = user.bot

    return user_type

# Function that returns the time the account was created
async def get_user_creationtime (user : discord.Member):
    user_creationtime = user.created_at

    return user_creationtime

# Function that returns the time the user joined the server
async def get_user_joinedtime (user : discord.Member):
    user_joinedtime = user.joined_at

    return user_joinedtime
