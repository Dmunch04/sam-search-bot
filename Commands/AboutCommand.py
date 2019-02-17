import discord
from discord.ext import commands

class CMD_About:
    def __init__ (self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def about (self, ctx):
        print("works")
