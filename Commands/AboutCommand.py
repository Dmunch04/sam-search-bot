import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed

class CMD_About:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def about (self, ctx):
        channel = ctx.message.channel
        await embed.ResultEmbed("Title", "Content", "https://google.com", channel)

def setup (client):
    client.add_cog(CMD_About(client))
