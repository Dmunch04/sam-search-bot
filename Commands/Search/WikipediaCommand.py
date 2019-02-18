import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed
import wikipedia as wp

class CMD_Wikipedia:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def wiki (self, ctx, *searchItem):
        channel = ctx.message.channel

        search = ""
        for word in searchItem:
            search += word
            search += " "

        if search == "":
          await embed.SpecifyErrorEmbed(self.client, channel)
        else:
          try:
            search = search.replace('[', '')
            search = search.replace(']', '')

            result = wp.page(search)
            print(result)

            await embed.ResultEmbed(self.client, result.title, result.content[:50] + '...', result.url, channel)
          except:
            await embed.UnknownErrorEmbed(self.client, channel)

def setup (client):
    client.add_cog(CMD_Wikipedia(client))
