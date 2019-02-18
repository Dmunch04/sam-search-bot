import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed

class CMD_Stackoverflow:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def stack (self, ctx, *searchItem):
        channel = ctx.message.channel

        await embed.CustomErrorEmbed(self.client, 'Command Error', 'Stack Command', 'Whoops! Looks like this command is under maintenance :(')

        return

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

            #result =

            await embed.ResultEmbed(self.client, result.title, result.content[:50] + '...', result.url, channel)
          except:
            await embed.UnknownErrorEmbed(self.client, channel)

def setup (client):
    client.add_cog(CMD_Stackoverflow(client))
