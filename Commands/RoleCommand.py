import discord
from discord.ext import commands
from Helpers import EmbedHelper as embed
from Helpers import ServerHelper as serverHelper

class CMD_Role:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def role (self, ctx, *roleAdd):
        channel = ctx.message.channel

        role = ""
        for word in roleAdd:
            role += word
            role += " "

        role = role.lower()

        server = serverHelper.get_server(ctx)

        threed = discord.utils.get(server.roles, name="3D Artist")
        twod = discord.utils.get(server.roles, name="2D Artist")
        pixel = discord.utils.get(server.roles, name="Pixel Artist")
        programmer = discord.utils.get(server.roles, name="Dev")
        musician = discord.utils.get(server.roles, name="Musician")
        writer = discord.utils.get(server.roles, name="Writer")
        voice = discord.utils.get(server.roles, name="voice artist")
        indie = discord.utils.get(server.roles, name="Indie")

        if role == "":
            await embed.SpecifyErrorEmbed(self.client, channel)
        elif role == "3d artist":
            await client.add_roles(sender, threed)
            await embed.OtherEmbed(self.client, 'Role Added', "Cool! You're a 3D Artist!", 'The role "3D Artist" has been added to your roles!', discord.Color.green(), channel)
        elif role == "2d artist":
            await client.add_roles(sender, twod)
            await embed.OtherEmbed(self.client, 'Role Added', "Cool! You're a 2D Artist!", 'The role "2D Artist" has been added to your roles!', discord.Color.green(), channel)
        elif role == "pixel artist":
            await client.add_roles(sender, pixel)
            await embed.OtherEmbed(self.client, 'Role Added', "Cool! You're a Pixel Artist!", 'The role "Pixel Artist" has been added to your roles!', discord.Color.green(), channel)
        elif role == "programmer":
            await client.add_roles(sender, programmer)
            await embed.OtherEmbed(self.client, 'Role Added', "Cool! You're a Programmer!", 'The role "Dev" has been added to your roles!', discord.Color.green(), channel)
        elif role == "musician":
            await client.add_roles(sender, musician)
            await embed.OtherEmbed(self.client, 'Role Added', "Cool! You're a Musician!", 'The role "Musician" has been added to your roles!', discord.Color.green(), channel)
        elif role == "writer":
            await client.add_roles(sender, writer)
            await embed.OtherEmbed(self.client, 'Role Added', "Cool! You're a Writer!", 'The role "Writer" has been added to your roles!', discord.Color.green(), channel)
        elif role == "voice":
            await client.add_roles(sender, voice)
            await embed.OtherEmbed(self.client, 'Role Added', "Cool! You're a Voice Artist!", 'The role "Voice Artist" has been added to your roles!', discord.Color.green(), channel)
        elif role == "indie":
            await client.add_roles(sender, indie)
            await embed.OtherEmbed(self.client, 'Role Added', "Cool! You're an Indie!", 'The role "Indie" has been added to your roles!', discord.Color.green(), channel)
        else:
            await embed.CustomErrorEmbed(self.client, 'Command Error', 'Role not found', "Hmm. Can't seem to find that role. Make sure to type it correctly. Do !roles to see all roles")

    @commands.command(pass_context = True)
    async def roles (self, ctx):
        channel = ctx.message.channel

        await embed.AnnouncementEmbed(self.client, 'These are the available roles:', '- 3D Artist\n- 2D Artist\n- Pixel Artist\n- Programmer\n- Musician\n- Writer\n- Voice Artist\n- Indie', channel)

def setup (client):
    client.add_cog(CMD_Role(client))
