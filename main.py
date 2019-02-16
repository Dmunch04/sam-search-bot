import os
import shutil
import json
from discord.ext import commands
import urbandictionary as ud
from google import google
import wikipedia as wp
import stackoverflow as so
import docsearcher as ds

TOKEN = os.environ['token']
Client = discord.Client()
client = commands.Bot(command_prefix = '!')

client.remove_command('help')

# -- EVENTS --

@client.event
async def on_ready ():
    await client.change_presence(game=discord.Game(name='!help'))
    print("Bot's been booted up. Awaiting user interaction")

@client.event
async def on_member_join (member):
    print("A member joined. Create user folder and user file")
    # Connect to DB and create a user folder (username#usertag) and a user file (User File.json) under the Users folder

@client.event
async def on_member_leave (member):
    print("A member left. Delete user folder and all it's content")
    # Connect to DB and delete the users folder and all the folders content

@client.event
async def on_server_join (server):
    try:
        embed = discord.Embed(
            colour = discord.Colour.purple()
        )

        for channel in server.channels:
            if channel.name == 'hangout':


            embed.set_author(name = 'Hello!')
            embed.add_field(name = 'Me', value = "Hey there! I'm Sam the Searcher, but you can just call me Sam. I'll help you search around on the internet. Do !help to get started!", inline = False)

            await client.send_message(channel, embed=embed)
    except:
        return

# -- COMMANDS

@client.command(pass_context = True)
async def help (ctx):
    sender = ctx.message.author
    channel = ctx.message.channel

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )

    if 'Staff' in [y.name.lower() for y in sender.roles]:
        embed.set_author(name = 'Help')
        embed.add_field(name = '!help', value = 'Shows the commands', inline = False)
        embed.add_field(name = '!urban [Search]', value = 'Searches Urban Dictionary for the search item', inline = False)
        embed.add_field(name = '!google [Search]', value = 'Searches Google for the search item [Not working atm]', inline = False)
        embed.add_field(name = '!wiki [Search]', value = 'Searches Wikipedia for the search item', inline = False)
        embed.add_field(name = '!stack [Search]', value = 'Searches Stackoveflow for the search item [Not working atm]', inline = False)
        embed.add_field(name = '!manual [Search]', value = 'Searches Unity Manual for the search item', inline = False)
        embed.add_field(name = '!script [Search]', value = 'Searches Unity Script API for the search item', inline = False)

        await client.send_message(channel, embed=embed)
    else:
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

      embed_success.set_author(name = 'We found a result')
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
async def google (ctx, search = ""):
  sender = ctx.message.author
  channel = ctx.message.channel

  embed_success = discord.Embed(
    colour = discord.Colour.green()
  )

  embed_error = discord.Embed(
    colour = discord.Colour.red()
  )

  if channel = ctx.message.channel:
      embed_success.set_author(name = 'Not working')
      embed_success.add_field(name = 'Google Command', value = "Looks like this command is not working. Please be patient and wait for an update!", inline = False)

      await client.send_message(channel, embed=embed_error)

      return

  if search == "":
    embed_error.set_author(name = 'Error')
    embed_error.add_field(name = 'Specify', value = 'Please specify what you wanna search for!', inline = False)

    await client.send_message(channel, embed=embed_error)
  else:
    try:
      #results = google.search(search)

      embed_success.set_author(name = 'We found a result')
      embed_success.add_field(name = 'Name:', value = results.name, inline = False)
      embed_success.add_field(name = 'Description :', value = results.description, inline = False)
      embed_success.add_field(name = 'Link:', value = results.link, inline = False)
      embed_success.add_field(name = 'Found results of' + "'{}'".format(search) + ':', value = results.number_of_results, inline = False)

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
        result = wiki.page(search)

        embed_success.set_author(name = 'We found a result')
        embed_success.add_field(name = 'Name:', value = result.title, inline = False)
        embed_success.add_field(name = 'Description:', value = result.content, inline = False)
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

        embed_success.set_author(name = 'We found a result')
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

        embed_success.set_author(name = 'We found a result')
        embed_success.add_field(name = 'Name:', value = result.title, inline = False)
        embed_success.add_field(name = 'Description :', value = result.description, inline = False)
        embed_success.add_field(name = 'Link:', value = result.url, inline = False)

        await client.send_message(channel, embed=embed_success)
      except:
        embed_error.set_author(name = 'Error')
        embed_error.add_field(name = 'Something went wrong..', value = "Looks like you did something wrong, or the page doesn't exist? ¯\_(ツ)_/¯", inline = False)

        await client.send_message(channel, embed=embed_error)

@client.command(pass_context = True)
async def stack (ctx, search = ""):
    sender = ctx.message.author
    channel = ctx.message.channel

    embed_success = discord.Embed(
      colour = discord.Colour.green()
    )

    embed_error = discord.Embed(
      colour = discord.Colour.red()
    )

    if channel = ctx.message.channel:
        embed_success.set_author(name = 'Not working')
        embed_success.add_field(name = 'Stackoverflow Command', value = "Looks like this command is not working. Please be patient and wait for an update!", inline = False)

        await client.send_message(channel, embed=embed_error)

        return

    if search == "":
      embed_error.set_author(name = 'Error')
      embed_error.add_field(name = 'Specify', value = 'Please specify what you wanna search for!', inline = False)

      await client.send_message(channel, embed=embed_error)
    else:
      try:
        #result = so.search(search)

        embed_success.set_author(name = 'We found a result')
        embed_success.add_field(name = 'Title:', value = result.title, inline = False)
        embed_success.add_field(name = 'Author:', value = result.sender, inline = False)
        embed_success.add_field(name = 'Tag(s):', value = result.tags, inline = False)
        embed_success.add_field(name = 'Link:', value = result.url, inline = False)
        embed_success.add_field(name = 'Is Answered:', value = result.answered, inline = False)
        embed_success.add_field(name = 'Answers:', value = result.answers, inline = False)

        await client.send_message(channel, embed=embed_success)
      except:
        embed_error.set_author(name = 'Error')
        embed_error.add_field(name = 'Something went wrong..', value = "Looks like you did something wrong, or the page doesn't exist? ¯\_(ツ)_/¯", inline = False)

        await client.send_message(channel, embed=embed_error)
