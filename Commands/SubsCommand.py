import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed
from Modules import SubCount as count

class CMD_Subs:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def subs (self, ctx):
        channel = ctx.message.channel
        embed.OtherEmbed(self.client, 'Make Indies subscriber count', 'This is the current amount of subscribers, Make Indies YouTube channels has:', count.getSubs(), discord.Color.green(), channel)

def setup (client):
    client.add_cog(CMD_Subs(client))
