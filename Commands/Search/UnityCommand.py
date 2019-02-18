import sys
import json
import discord
from discord.ext import commands
import docssearcher as ds
import EmbedHelper as embed

class CMD_Unity:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def manual (self, ctx, *searchItem):
        sender = ctx.message.author
        channel = ctx.message.channel

        embed_error = discord.Embed(
          color = discord.Color.red()
        )

        search = ""
        for word in searchItem:
            search += word
            search += " "

        if search == "":
          embed_error.set_author(name = 'Error')
          embed_error.add_field(name = 'Specify', value = 'Please specify what you wanna search for!', inline = False)

          await self.client.send_message(channel, embed=embed_error)
        else:
          try:
            search = search.replace('[', '')
            search = search.replace(']', '')

            searchResult = ds.search(search, 'manual')

            await embed.ResultEmbed(searchResult.title, result.description, result.url, channel)
          except:
            embed_error.set_author(name = 'Error')
            embed_error.add_field(name = 'Something went wrong..', value = "Looks like you did something wrong, or the page doesn't exist? ¯\_(ツ)_/¯", inline = False)

            await self.client.send_message(channel, embed=embed_error)

    @commands.command(pass_context = True)
    async def script (self, ctx, *searchItem):
        sender = ctx.message.author
        channel = ctx.message.channel

        embed_error = discord.Embed(
          color = discord.Color.red()
        )

        search = ""
        for word in searchItem:
            search += word
            search += " "

        if search == "":
          embed_error.set_author(name = 'Error')
          embed_error.add_field(name = 'Specify', value = 'Please specify what you wanna search for!', inline = False)

          await self.client.send_message(channel, embed=embed_error)
        else:
          try:
            search = search.replace('[', '')
            search = search.replace(']', '')

            searchResult = ds.search(search, 'script')

            await embed.ResultEmbed(searchResult.title, result.description, result.url, channel)
          except:
            embed_error.set_author(name = 'Error')
            embed_error.add_field(name = 'Something went wrong..', value = "Looks like you did something wrong, or the page doesn't exist? ¯\_(ツ)_/¯", inline = False)

            await self.client.send_message(channel, embed=embed_error)

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
