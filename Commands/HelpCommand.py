import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed

class CMD_Help:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def help (self, ctx):
        await embed.HelpEmbed(self.client, channel)

def setup (client):
    client.add_cog(CMD_Help(client))
