import json
import requests
from player import Player


def initialize():
    nhl_roster = requests.get("https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster")
    data = json.loads(nhl_roster.text)
    teams = json.loads(json.dumps(data["teams"][0:32]))

    players = []

    for team in range(len(teams)):
        size = len(teams[team]["roster"]["roster"])
        
        for p in range(size):
            print(teams[team]["roster"]["roster"][p]["person"]["id"])
            players.append(Player(teams[team]["roster"]["roster"][p]["person"]["id"]))


    f = open("players.txt", "w")

    for x in players:
        f.write(x.player_info_short())

    f.close()

    return True

def player_list():

    f = open("players.txt", "r")

    lines = []
    line = f.readline()

    while(line != ""):

        temp = line.rstrip("\n").split(",")

        lines.append([int(temp[0]), temp[1], temp[2]])

        line = f.readline()

    f.close()

    return lines


def abbr_to_team(abbr):

    f = open("teams.txt", "r")
    
    temp = []
    line = f.readline()

    while(line != ""):
        temp = line.split(",")
        temp[1] = temp[1].rstrip("\n")
        if(abbr.lower() == temp[1]):
            break

        line = f.readline()

    f.close()

    return temp[0]

def get_player_info(firstname, lastname):

    players = player_list()

    player = None

    for x in players:
        if(x[1] == firstname.lower() + " " + lastname.lower()):

            player = Player(x[0])
            break

    return player



