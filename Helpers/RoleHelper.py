import discord

# Function that returns a role
async def get_role (server, role_name):
    role = discord.utils.get(server.roles, name = role_name)

    return role

# Function that returns the servers default role
async def get_default_role (server):
    default_role = server.default_role

    return default_role

# Function that returns the roles name
async def get_role_name (role):
    role_name = role.name

    return role_name

# Function that returns mention for the role
async def get_role_mention (role):
    role_mention = role.mention

    return role_mention

# Function that returns the roles id
async def get_role_id (role):
    role_id = role.id

    return role_id

# Function that returns the roles server
async def get_role_server (role):
    role_server = role.server

    return role_server

# Function that returns all the roles permissions
async def get_role_permissions (role):
    role_permissions = role.permissions

    return role_permissions

# Function that returns the roles position in the role hierarchy
async def get_role_position (role):
    role_position = role.position

    return role_position

# Function that returns the roles color
async def get_role_color (role):
    role_color = role.colour

    return role_color

# Function that returns a bool whether the role is mentionable or not
async def get_role_mentionable (role):
    role_is_mentionable = role.mentionable

    return role_is_mentionable

# Function that returns the time the role was created
async def get_role_timecreated (role):
    role_time_created = role.created_at

    return role_time_created
