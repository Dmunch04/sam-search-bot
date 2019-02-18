import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed

class CMD_Update:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def update (self, ctx, version):
        author = ctx.message.author
        channel = ctx.message.channel

        if not 'Bot Dev' in [y.name.lower() for y in author.roles]:
            await embed.CustomErrorEmbed(self.client, 'User Error', 'Permission not found', "Looks like you don't have the permissions to do that, buddy.", channel)
            return

        newVersionFile = open('newVersion.txt', 'r')
        newVersion = newVersionFile.read()
        newVersionFile.close()

        curVersionFile = open('currentVersion.txt', 'r')
        curVersion = curVersionFile.read()
        curVersionFile.close()

        if curVersion == newVersion:
            return
        else:
            changelogFile = open('changelog.txt', 'r')
            changes = changelogFile.read()
            changelogFile.close()

            await embed.AnnouncementEmbed(self.client, 'Uuh! A new update has arrived ({0})'.format(version), changes, channel)

            curVersionFile = open('currentVersion.txt', 'w')
            curVersionFile.write(newVersion)
            curVersionFile.close()

    async def checkVersion ():
        newVersionFile = open('Commands.Staff.newVersion.txt', 'r')
        newVersion = newVersionFile.read()
        newVersionFile.close()

        curVersionFile = open('Data.currentVersion.txt', 'r')
        curVersion = curVersionFile.read()
        curVersionFile.close()

        if curVersion == newVersion:
            return
        else:
            await update.callback(newVersion)

def setup (client):
    client.add_cog(CMD_Update(client))
