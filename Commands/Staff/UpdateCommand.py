import asyncio
import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed
from Helpers import ServerHelper as serverhelp

cur_server = ""

class CMD_Update:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def update (self, ctx):
        global cur_server

        author = ctx.message.author
        cur_server = await shelp.get_server(ctx)

        if not 'bot dev' in [y.name.lower() for y in author.roles]:
            await embed.CustomErrorEmbed(self.client, 'User Error', 'Permission not found', "Looks like you don't have the permissions to do that, buddy.", channel)
            return

        await self.updateBot()

    async def updateBot (self):
        global cur_server

        try:
            cur_server
        except NameError:
            print('Update Manually!')
            return

        channel = await serverhelp.get_server_channel(cur_server, 'bot-updates')

        newVersionFile = open('Data/newVersion.txt', 'r')
        newVersion = newVersionFile.read()
        newVersionFile.close()

        curVersionFile = open('Data/currentVersion.txt', 'r')
        curVersion = curVersionFile.read()
        curVersionFile.close()

        changelogFile = open('Data/changelog.txt', 'r')
        changes = changelogFile.read()
        changelogFile.close()

        if curVersion == newVersion:
            return
        else:
            await embed.AnnouncementEmbed(self, 'Uuh! A new update has arrived ({0})'.format(newVersion), changes, channel)

            curVersionFile = open('Data/currentVersion.txt', 'w')
            curVersionFile.write(newVersion)
            curVersionFile.close()

def setup (client):
    client.add_cog(CMD_Update(client))
