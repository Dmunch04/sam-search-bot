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

        channel = count.getChannel()

        await embed.ResultLinkEmbed(self.client, 'Make Indies subscriber count', channel.name, channel.link, "Make Indies YouTube channel's current amount of subscribers: " + channel.subs, channel)

def setup (client):
    client.add_cog(CMD_Subs(client))
