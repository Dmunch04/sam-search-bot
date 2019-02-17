import sys
import os
import shutil
import json
import time
import datetime
import discord
from discord.ext import commands
import urbandictionary as ud
import wikipedia as wp
import docssearcher as ds

if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote as urlquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote as urlquote

TOKEN = os.environ['botToken']
Client = discord.Client()
client = commands.Bot(command_prefix = '!')

client.remove_command('help')

URL_VERSION = 'http://munchii.me/searcher-sam/version.txt'
URL_CHANGELOG = 'http://munchii.me/searcher-sam/changelog.txt'

#commands = ['AboutCommand', 'ChallengeCommand', 'ChangelogCommand', 'HelpCommand', 'LeaderboardCommand', 'RoleCommand', 'RulesCommand', 'StatsCommand', 'ThanksCommand', 'GoogleCommand', 'StackoveflowCommand', 'UnityCommand', 'UrbanDictionaryCommand', 'WikipediaCommand', 'BanCommand', 'KickCommand', 'MuteCommand']
commands = ['UnityCommand']

# -- EVENTS --

@client.event
async def on_ready ():
    await client.change_presence(game=discord.Game(name='!help'))
    print("Bot's been booted up. Awaiting user interaction")

    await checkVersion()

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
    embed.add_field(name = '!role [Role]', value = 'Use this command to add a role to yourself', inline = False)
    embed.add_field(name = '!roles', value = 'Shows you all the roles you can join', inline = False)

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
        search = search.replace('[', '')
        search = search.replace(']', '')

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

@client.command(pass_context = True)
async def role (ctx, role = ""):
  sender = ctx.message.author
  channel = ctx.message.channel
  server = ctx.message.server

  role = role.lower()

  embed_success = discord.Embed(
      colour = discord.Colour.green()
    )

  embed_error = discord.Embed(
    colour = discord.Colour.red()
  )

  threed = discord.utils.get(server.roles, name="3D Artist")
  twod = discord.utils.get(server.roles, name="2D Artist")
  pixel = discord.utils.get(server.roles, name="Pixel Artist")
  programmer = discord.utils.get(server.roles, name="Dev")
  musician = discord.utils.get(server.roles, name="Musician")
  writer = discord.utils.get(server.roles, name="Writer")
  voice = discord.utils.get(server.roles, name="voice artist")
  indie = discord.utils.get(server.roles, name="Indie")

  if role == "":
    embed_error.set_author(name = 'Error')
    embed_error.add_field(name = 'Specify which role you want:', value = '- 3D Artist\n- 2D Artist\n- Pixel Artist\n- Programmer\n- Musician\n- Writer\n- Voice Artist\n- Indie', inline = False)
    await client.send_message(channel, embed=embed_error)
  elif role == "3d":
    print("works")
    await client.add_roles(sender, threed)
    embed_success.set_author(name = 'Role Added')
    embed_success.add_field(name = "Cool! You're a 3D Artist!", value = 'Yay!', inline = False)
    await client.send_message(channel, embed=embed_success)
  elif role == "2d":
    await client.add_roles(sender, twod)
    embed_success.set_author(name = 'Role Added')
    embed_success.add_field(name = "Cool! You're a 2D Artist!", value = 'Yay!', inline = False)
    await client.send_message(channel, embed=embed_success)
  elif role == "pixel":
    await client.add_roles(sender, pixel)
    embed_success.set_author(name = 'Role Added')
    embed_success.add_field(name = "Cool! You're a Pixel Artist!", value = 'Yay!', inline = False)
    await client.send_message(channel, embed=embed_success)
  elif role == "programmer":
    await client.add_roles(sender, programmer)
    embed_success.set_author(name = 'Role Added')
    embed_success.add_field(name = "Cool! You're a Programmer!", value = 'Yay!', inline = False)
    await client.send_message(channel, embed=embed_success)
  elif role == "musician":
    await client.add_roles(sender, musician)
    embed_success.set_author(name = 'Role Added')
    embed_success.add_field(name = "Cool! You're a Musician!", value = 'Yay!', inline = False)
    await client.send_message(channel, embed=embed_success)
  elif role == "writer":
    await client.add_roles(sender, writer)
    embed_success.set_author(name = 'Role Added')
    embed_success.add_field(name = "Cool! You're a Writer!", value = 'Yay!', inline = False)
    await client.send_message(channel, embed=embed_success)
  elif role == "voice":
    await client.add_roles(sender, voice)
    embed_success.set_author(name = 'Role Added')
    embed_success.add_field(name = "Cool! You're a Voice Artist Artist!", value = 'Yay!', inline = False)
    await client.send_message(channel, embed=embed_success)
  elif role == "indie":
    await client.add_roles(sender, indie)
    embed_success.set_author(name = 'Role Added')
    embed_success.add_field(name = "Cool! You're an Indie!", value = 'Yay!', inline = False)
    await client.send_message(channel, embed=embed_success)

@client.command(pass_context = True)
async def roles (ctx):
  sender = ctx.message.author
  channel = ctx.message.channel

  embed_info = discord.Embed(
    colour = 0x2a2a2a
  )

  embed_info.set_author(name = 'Roles')
  embed_info.add_field(name = 'These are the roles you can join:', value = '- 3D Artist\n- 2D Artist\n- Pixel Artist\n- Programmer\n- Musician\n- Writer\n- Voice Artist\n- Indie', inline = False)

  await client.send_message(channel, embed=embed_info)

@client.command()
async def updateMsg ():
  changes = urlopen(URL_CHANGELOG).read().decode('utf-8')
  version = urlopen(URL_VERSION).read().decode('utf-8')

  channel = discord.utils.get(client.get_all_channels(), server__name = 'Make Indies', name = 'bot-updates')

  embed_announcement = discord.Embed(
    colour = 0x2a2a2a
  )

  embed_announcement.set_author(name = 'Uuh! A new update ({0})'.format(version))
  embed_announcement.add_field(name = 'Changes:', value = changes, inline = False)
  #embed_announcement.add_field(name = 'Changes:', value = '- Added a role command\n- Fixed bugs', inline = False)

  await client.send_message(channel, embed=embed_announcement)

async def checkVersion ():
    version = urlopen(URL_VERSION).read().decode('utf-8')

    # Check if version is not equal to the current version.

    #await updateMsg.callback()

if __name__ == '__main__':
    for command in commands:
        try:
            client.load_extension(command)
        except Exception as error:
            print('{0} cannot be loaded. Error: {0}'.format(command, error))

    client.run(TOKEN)
