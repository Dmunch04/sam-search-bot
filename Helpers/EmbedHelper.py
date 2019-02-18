import discord

# Embeds

# Embed for positive search results
async def ResultLinkEmbed (client, title, content, link, channel):
    embed = discord.Embed(title = title, url = link, description = content, color = discord.Color.green())
    embed.set_author(name = 'I found a result!')

    await client.send_message(channel, embed = embed)

# Embed for when an urban dictionary result is found. This needs a custom template
async def UrbanEmbed (client, word, definition, example, upvotes, downvotes, channel):
    embed = discord.Embed(color = discord.Color.green())
    embed.set_author(name = 'I found a result')
    embed.add_field(name = 'Searched word:', value = word, inline = False)
    embed.add_field(name = 'Definition:', value = definition, inline = False)
    embed.add_field(name = 'Usage Example:', value = example, inline = False)
    embed.add_field(name = 'Rating:', value = '👍{}    👎{}'.format(upvotes, downvotes), inline = False)

    await client.send_message(channel, embed = embed)

# Embed for the error: Specify Error (When you don't specify what you wanna search for)
async def SpecifyErrorEmbed (client, channel):
    embed = discord.Embed(title = 'Specify Search', description = 'Please specify what you wanna search for!', color = discord.Color.red())
    embed.set_author(name = 'Command Error')

    await client.send_message(channel, embed = embed)

# Embed for the error : Unknown Error (When no one knows the error)
async def UnknownErrorEmbed (client, channel):
    embed = discord.Embed(title = 'Something went wrong..', description = 'Whoops! Looks like something went wrong.', color = discord.Color.red())
    embed.set_author(name = 'Command Error')

    await client.send_message(channel, embed = embed)

# Embed for a custom error. This can be anything
async def CustomErrorEmbed (client, title, errorTitle, error, channel):
    embed = discord.Embed(title = errorTitle, description = error, color = discord.Color.red())
    embed.set_author(name = title)

    await client.send_message(channel, embed = embed)

# Embed for announcement messages
async def AnnouncementEmbed (client, title, message, channel):
    embed = discord.Embed(title = title, description = message, color = 0x2a2a2a)

    await client.send_message(channel, embed = embed)

# Embed for the help message. This needs a custom template (Maybe make a JSON file later and make it read it)
async def HelpEmbed (client, channel):
    embed = discord.Embed(color = discord.Color.purple())
    embed.set_author(name = 'Help')
    embed.add_field(name = '!help', value = 'Shows the commands', inline = False)
    embed.add_field(name = '!rules', value = 'Shows the rules', inline = False)
    embed.add_field(name = '!about', value = 'Sends a message explaining about the bot', inline = False)
    embed.add_field(name = '!urban [Search]', value = 'Searches Urban Dictionary for the search item', inline = False)
    embed.add_field(name = '!google [Search]', value = 'Searches Google for the search item [Not working atm]', inline = False)
    embed.add_field(name = '!wiki [Search]', value = 'Searches Wikipedia for the search item', inline = False)
    embed.add_field(name = '!stack [Search]', value = 'Searches Stackoveflow for the search item [Not working atm]', inline = False)
    embed.add_field(name = '!manual [Search]', value = 'Searches Unity Manual for the search item', inline = False)
    embed.add_field(name = '!script [Search]', value = 'Searches Unity Script API for the search item', inline = False)
    embed.add_field(name = '!role [Role]', value = 'Use this command to add a role to yourself', inline = False)
    embed.add_field(name = '!roles', value = 'Shows you all the roles you can join', inline = False)

# Embed for other embed messages. This can be anything
async def OtherEmbed (client, title, messageTitle, message, color, channel):
    embed = discord.Embed(title = messageTitle, description = message, color = color)
    embed.set_author(name = title)

    await client.send_message(channel, embed = embed)
