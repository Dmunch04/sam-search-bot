import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed
import urbandictionary as ud

class CMD_UrbanDictionary:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def urban (self, ctx, *searchItem):
        author = ctx.message.author
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

            definitions = ud.define(search)

            definition = definitions[0]

            definition.word = definition.word.replace('[', '')
            definition.word = definition.word.replace(']', '')
            definition.definition = definition.definition.replace('[', '')
            definition.definition = definition.definition.replace(']', '')
            definition.example = definition.example.replace('[', '')
            definition.example = definition.example.replace(']', '')

            await embed.UrbanEmbed(self.client, definition.word, definition.definition, definition.example, definition.upvotes, definition.downvotes, channel)
          except:
            await embed.UnknownErrorEmbed(self.client, channel)

def setup (client):
    client.add_cog(CMD_UrbanDictionary(client))
