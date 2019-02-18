import discord

# Function that returns the sender of the message
async def get_message_author (message):
    message_author = message.author

    return message_author

# Function that returns the content of the message
async def get_message_content (message):
    message_content = message.content

    return message_content

# Function that returns the channel the message was sent in
async def get_message_channel (message):
    message_channel = message.channel

    return message_channel

# Function that returns the server the message was sent in
async def get_message_server (message):
    message_server = message.server

    return message_server

# Function that returns the time the message was sent
async def get_message_time_sent (message):
    message_time_sent = message.timestamp

    return message_time_sent

# Function that returns the time the message was edited
async def get_message_time_edited (message):
    message_time_edited = message.edited_timestamp

    return message_time_edited

# Function that returns a bool whether the message was text to speech or not
async def get_message_tts (message):
    message_tts = message.tts

    return message_tts

# Function that returns a list of the embedded objects in the message
async def get_message_embeds (message):
    message_embeds = messages.embeds

    return message_embeds

# Function that returns all the reactions to the message
async def get_message_reactions (message):
    message_reactions = message.reactions

    return message_reactions

# Function that returns a bool whether the message is pinned or not
async def get_message_is_pinned (message):
    message_is_pinned = message.pinned

    return message_is_pinned

# Function that returns the id of the message
async def get_message_id (message):
    message_id = message.id

    return message_id

# Funtion that returns all the user mentions in the given message
async def get_message_user_mentions (message):
    message_user_mentions = message.mentions

    return message_user_mentions

# Function that returns all the channel mentions in the given message
async def get_message_channel_mentions (message):
    message_channel_mentions = message.channel_mentions

    return message_channel_mentions

# Function that returns all the role mentions in the given message
async def get_message_role_mentions (message):
    message_role_mentions = message.role_mentions

    return message_role_mentions
