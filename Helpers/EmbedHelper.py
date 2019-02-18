import discord

async def ResultEmbed (title, content, link, channel):
    embed = discord.Embed(title = title, url = link, description = content)
    await self.client.send_message(channel, embed)
