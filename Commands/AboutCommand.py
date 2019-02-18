import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed

class CMD_About:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def about (self, ctx):
        channel = ctx.message.channel
        await embed.OtherEmbed(self.client, 'About', 'About me, Boto', "Hello guys! My name is Boto. I'm the helper of Make Indies. My best buddy, Munchii, is the one that learned me everything I know. The important thing: I'm always here to help. To get my help, do !help", discord.Color.blue(), channel)

def setup (client):
    client.add_cog(CMD_About(client))
