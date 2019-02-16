import os
import shutil
import json
import discord
from discord.ext import commands
import urbandictionary as ud
import wikipedia as wp
import docssearcher as ds

#TOKEN = os.environ['token']
TOKEN = 'NTQ2MDA4NDgzNDY4NjczMDI4.D0m94g.Y6sG8dPNPWDjU2oswetdxZy_SuE'
Client = discord.Client()
client = commands.Bot(command_prefix = '!')

client.remove_command('help')

# -- EVENTS --

@client.event
async def on_ready ():
    await client.change_presence(game=discord.Game(name='!help'))
    print("Bot's been booted up. Awaiting user interaction")

# -- COMMANDS

@client.command(pass_context = True)
async def help (ctx):
    sender = ctx.message.author
    channel = ctx.message.channel

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )
    
    embed.set_author(name = 'Help')
    embed.add_field(name = '!help', value = 'Shows the commands', inline = False)
    embed.add_field(name = '!urban [Search]', value = 'Searches Urban Dictionary for the search item', inline = False)
    embed.add_field(name = '!google [Search]', value = 'Searches Google for the search item [Not working atm]', inline = False)
    embed.add_field(name = '!wiki [Search]', value = 'Searches Wikipedia for the search item', inline = False)
    embed.add_field(name = '!stack [Search]', value = 'Searches Stackoveflow for the search item [Not working atm]', inline = False)
    embed.add_field(name = '!manual [Search]', value = 'Searches Unity Manual for the search item', inline = False)
    embed.add_field(name = '!script [Search]', value = 'Searches Unity Script API for the search item', inline = False)

    await client.send_message(channel, embed=embed)

@client.command(pass_context = True)
async def urban (ctx, search = ""):
  sender = ctx.message.author
  channel = ctx.message.channel

  embed_success = discord.Embed(
    colour = discord.Colour.green()
  )

  embed_error = discord.Embed(
    colour = discord.Colour.red()
  )

  if search == "":
    embed_error.set_author(name = 'Error')
    embed_error.add_field(name = 'Specify', value = 'Please specify what you wanna search for!', inline = False)

    await client.send_message(channel, embed=embed_error)
  else:
    try:
      definitions = ud.define(search)

      definition = definitions[0]

      embed_success.set_author(name = 'I found a result')
      embed_success.add_field(name = 'Searched word:', value = definition.word, inline = False)
      embed_success.add_field(name = 'Definition:', value = definition.definition, inline = False)
      embed_success.add_field(name = 'Usage Example:', value = definition.example, inline = False)
      embed_success.add_field(name = 'Rating:', value = '👍{}   👎{}'.format(definition.upvotes, definition.downvotes), inline = False)

      await client.send_message(channel, embed=embed_success)
    except:
      embed_error.set_author(name = 'Error')
      embed_error.add_field(name = 'Something went wrong..', value = 'Please make sure you did everything correct!', inline = False)

      await client.send_message(channel, embed=embed_error)

@client.command(pass_context = True)
async def wiki (ctx, search = ""):
    sender = ctx.message.author
    channel = ctx.message.channel

    embed_success = discord.Embed(
      colour = discord.Colour.green()
    )

    embed_error = discord.Embed(
      colour = discord.Colour.red()
    )

    if search == "":
      embed_error.set_author(name = 'Error')
      embed_error.add_field(name = 'Specify', value = 'Please specify what you wanna search for!', inline = False)

      await client.send_message(channel, embed=embed_error)
    else:
      try:
        result = wp.page(search)

        embed_success.set_author(name = 'I found a result')
        embed_success.add_field(name = 'Name:', value = result.title, inline = False)
        embed_success.add_field(name = 'Description:', value = result.content[:50] + '...', inline = False)
        embed_success.add_field(name = 'Link:', value = result.url, inline = False)

        await client.send_message(channel, embed=embed_success)
      except:
        embed_error.set_author(name = 'Error')
        embed_error.add_field(name = 'Something went wrong..', value = "Looks like you did something wrong, or the page doesn't exist? ¯\_(ツ)_/¯", inline = False)

        await client.send_message(channel, embed=embed_error)

@client.command(pass_context = True)
async def manual (ctx, search = ""):
    sender = ctx.message.author
    channel = ctx.message.channel

    embed_success = discord.Embed(
      colour = discord.Colour.green()
    )

    embed_error = discord.Embed(
      colour = discord.Colour.red()
    )

    if search == "":
      embed_error.set_author(name = 'Error')
      embed_error.add_field(name = 'Specify', value = 'Please specify what you wanna search for!', inline = False)

      await client.send_message(channel, embed=embed_error)
    else:
      try:
        result = ds.search(search, "manual")

        embed_success.set_author(name = 'I found a result')
        embed_success.add_field(name = 'Name:', value = result.title, inline = False)
        embed_success.add_field(name = 'Description :', value = result.description, inline = False)
        embed_success.add_field(name = 'Link:', value = result.url, inline = False)

        await client.send_message(channel, embed=embed_success)
      except:
        embed_error.set_author(name = 'Error')
        embed_error.add_field(name = 'Something went wrong..', value = "Looks like you did something wrong, or the page doesn't exist? ¯\_(ツ)_/¯", inline = False)

        await client.send_message(channel, embed=embed_error)

@client.command(pass_context = True)
async def script (ctx, search = ""):
    sender = ctx.message.author
    channel = ctx.message.channel

    embed_success = discord.Embed(
      colour = discord.Colour.green()
    )

    embed_error = discord.Embed(
      colour = discord.Colour.red()
    )

    if search == "":
      embed_error.set_author(name = 'Error')
      embed_error.add_field(name = 'Specify', value = 'Please specify what you wanna search for!', inline = False)

      await client.send_message(channel, embed=embed_error)
    else:
      try:
        result = ds.search(search, "script")

        embed_success.set_author(name = 'I found a result')
        embed_success.add_field(name = 'Name:', value = result.title, inline = False)
        embed_success.add_field(name = 'Description :', value = result.description, inline = False)
        embed_success.add_field(name = 'Link:', value = result.url, inline = False)

        await client.send_message(channel, embed=embed_success)
      except:
        embed_error.set_author(name = 'Error')
        embed_error.add_field(name = 'Something went wrong..', value = "Looks like you did something wrong, or the page doesn't exist? ¯\_(ツ)_/¯", inline = False)

        await client.send_message(channel, embed=embed_error)

@client.command(pass_context = True)
async def google (ctx, search = ""):
  sender = ctx.message.author
  channel = ctx.message.channel

  embed_error = discord.Embed(
    colour = discord.Colour.red()
  )

  embed_error.set_author(name = 'Not working')
  embed_error.add_field(name = 'Google Command', value = "Looks like this command is not working. Please be patient and wait for an update!", inline = False)

  await client.send_message(channel, embed=embed_error)

  return

@client.command(pass_context = True)
async def stack (ctx, search = ""):
  sender = ctx.message.author
  channel = ctx.message.channel

  embed_error = discord.Embed(
    colour = discord.Colour.red()
  )

  embed_error.set_author(name = 'Not working')
  embed_error.add_field(name = 'Stack Command', value = "Looks like this command is not working. Please be patient and wait for an update!", inline = False)

  await client.send_message(channel, embed=embed_error)

  return


if __name__ == '__main__':
    client.run(TOKEN)
