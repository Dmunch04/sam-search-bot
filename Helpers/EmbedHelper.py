import discord

async def ResultEmbed (client, title, content, link, channel):
    embed = discord.Embed(title = title, url = link, description = content)
    await client.send_message(channel, embed)
