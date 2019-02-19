import discord

# Function that returns the link of the invite
async def get_invite (invite):
    invite_link = invite.url

    return invite_link

# Function that returns the invites id
async def get_invite_id (invite):
    invite_id = invite.id

    return invite_id

# Function that returns the invites sender
async def get_invite_sender (invite):
    invite_sender = invite.inviter

    return invite_sender

# Function that returns the time left in seconds before the invite expires (0 is never expiring)
async def get_invite_expiration (invite):
    invite_expiration = invite.max_age

    return invite_expiration

# Function that returns the target server
async def get_invite_server (invite):
    invite_server = invite.server

    return invite_server

# Function that returns the time the invite was created
async def get_invite_time_created (invite):
    invite_time_created = invite.created_at

    return invite_time_created

# Function that returns a bool whether the invite has been used or not
async def get_invite_used (invite):
    invite_used = invited.revoked

    return invite_used

# Function that returns the amount of times the invite has been used
async def get_invite_uses (invite):
    invite_uses = invite.uses

    return invite_uses
