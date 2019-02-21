import os
import discord
from discord.ext import commands
from Commands.Staff.UpdateCommand import CMD_Update
from Data import testfile.txt

TOKEN = os.environ['botToken']
Client = discord.Client()
client = commands.Bot(command_prefix = '!')

client.remove_command('help')

commands = ['Commands.AboutCommand', 'Commands.ChallengeCommand', 'Commands.ChangelogCommand', 'Commands.HelpCommand', 'Commands.LeaderboardCommand', 'Commands.RoleCommand', 'Commands.RulesCommand', 'Commands.StatsCommand', 'Commands.ThanksCommand', 'Commands.Search.GoogleCommand', 'Commands.Search.StackoverflowCommand', 'Commands.Search.UnityCommand', 'Commands.Search.UrbanDictionaryCommand', 'Commands.Search.WikipediaCommand', 'Commands.Staff.BanCommand', 'Commands.Staff.KickCommand', 'Commands.Staff.MuteCommand', 'Commands.Staff.UpdateCommand']

@client.event
async def on_ready ():
    await client.change_presence(game=discord.Game(name='!help'))
    print("Bot's been booted up. Awaiting user interaction")

    await CMD_Update.checkVersion()

    f = open('Data.testfile.txt', 'r')
    content = f.read()
    f.close()

    print(content)

if __name__ == '__main__':
    for command in commands:
        try:
            client.load_extension(command)
        except Exception as error:
            print('{0} cannot be loaded. Error: {0}'.format(command, error))

    client.run(TOKEN)
