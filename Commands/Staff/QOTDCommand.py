import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed
from Helpers import ServerHelper as shelp
#from Modules import QOTD as qotd

class CMD_QOTD:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def qotd (self, ctx, *args = ""):
        channel = ctx.message.channel
        server = ctx.message.server

        qotd_channel = shelp.get_channel(server, 'qotd')

        arg = ""
        for word in args:
            arg += word
            arg += " "

        if arg == "":
            try:
                #result = qotd.getQuote()

                await embed.OtherEmbed(self.client, 'QOTD Message', '@everyone - Question (#{0})'.format(result.number), result.quote, discord.Color.green() channel)
            except:
                await embed.UnknownErrorEmbed(self.client, channel)
        else:
            try:
                data = open('Data/QOTDs.txt', 'w')
                data.write(arg + '\n')
                data.close()

                await embed.OtherEmbed(self.client, 'Success!', 'Successfully added a new QOTD!', "I've added '" + arg + "' to the QOTD list!", discord.Color.green(), channel)
            except:
                await embed.UnknownErrorEmbed(self.client, channel)

def setup (client):
    client.add_cog(CMD_QOTD(client))
