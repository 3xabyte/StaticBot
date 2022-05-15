from discord.ext import commands
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext

import functions

TOKEN = "OTc1NDE5NjUxNzE2NjgxNzQy.GttkTy.ufFd4ijApsdfyRIwAo9u3cs0aIoR2ipg1Wbb5s"

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")

@bot.command()
async def initialize(c):
    await c.send("Creating a new players.txt file. This will take a minute or two, please wait!")
    functions.initialize()
    await c.send("Players initialized!")
    
@bot.command()
async def bot_help(c):
    output = "!initialize - Initializes a new players.txt file containing the player ID, name, and team\n"
    output += "!bot_help - Prints this message\n"
    output += "!get_team_roster team_abbreviation (3 chars) - Gets a list of players on a team's roster\n"
    output += "!get_player_info firstname lastname - Gets information about a player"

    await c.send(output)

@bot.command()
async def get_team_roster(c, team_abbr):
    
    team = functions.abbr_to_team(team_abbr).lower()

    info = functions.player_list()
    output = ""
    
    for x in info:
        if(team in x):
            output += "{:}\n".format(x[1].title())

    await c.send(output)

@bot.command()
async def get_player_info(c, firstname, lastname):

    output = functions.get_player_info(firstname, lastname)

    await c.send(output)

bot.run(TOKEN)