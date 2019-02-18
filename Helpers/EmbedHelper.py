import discord

async def ResultEmbed (client, title, content, link, channel):
    embed = discord.Embed(title = title, url = link, description = content, color = discord.Color.green())
    await client.send_message(channel, embed = embed)
