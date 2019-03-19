import sys
import json
import discord
from discord.ext import commands
import docssearcher as ds
from Helpers import EmbedHelper as embed

class CMD_Unity:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def manual (self, ctx, *searchItem):
        sender = ctx.message.author
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

            searchResult = ds.search(str(search), 'manual')

            await embed.ResultLinkEmbed(self.client, searchResult.title, result.description, result.url, channel)
          except:
            await embed.UnknownErrorEmbed(self.client, channel)

    @commands.command(pass_context = True)
    async def script (self, ctx, *searchItem):
        sender = ctx.message.author
        channel = ctx.message.channel

        search = ""
        for word in searchItem:
            search += word
            search += " "

        print(str(search))

        searchResult = ds.search(str(search), 'script')

        await embed.ResultLinkEmbed(self.client, searchResult.title, result.description, result.url, channel)

        if search == "":
          await embed.SpecifyErrorEmbed(self.client, channel)
        else:
          try:
            search = search.replace('[', '')
            search = search.replace(']', '')

            searchResult = ds.search(search, 'script')

            await embed.ResultLinkEmbed(self.client, searchResult.title, result.description, result.url, channel)
          except:
            await embed.UnknownErrorEmbed(self.client, channel)

    # Acrhived command (Fix this later [The if statement never activates for some reason])
    async def search (self, docs, search, channel):
        rawData = urlopen(URL_SEARCH + docs + '.json').read().decode('utf-8')
        jsonData = json.loads(rawData)

        print(jsonData[0])

        for element in jsonData:
            if search in element['title']:
                embed_result = discord.Embed(title = element['title'], url = element['link'], description = element['description'])
                await self.client.send_message(channel, embed_result)

def setup (client):
    client.add_cog(CMD_Unity(client))
