import json
import requests

class Player:

    def __init__(self, id):
        stats = self._get_stats(id)

        self._id = id
        self._firstName = stats["firstName"]
        self._lastName = stats["lastName"]

        try:
            self._number = stats["primaryNumber"]
        except:
            self._number = None

        self._birthday = stats["birthDate"]
        self._age = stats["currentAge"]
        self._city = stats["birthCity"]

        try:
            self._province = stats["birthStateProvince"]
        except:
            self._province = None

        self._country = stats["birthCountry"]
        self._nationality = stats["nationality"]
        self._height = stats["height"]
        self._weight = stats["weight"]
        self._alt = stats["alternateCaptain"]
        self._cap = stats["captain"]
        self._shoots = stats["shootsCatches"]
        self._team = stats["currentTeam"]["name"]
        self._position = stats["primaryPosition"]["name"]


        return

    def _get_stats(self, id):

        player_api = requests.get("https://statsapi.web.nhl.com/api/v1/people/{:}".format(id))
        data = json.loads(player_api.text)
        person = json.loads(json.dumps(data["people"][0]))

        return person

    def __str__(self):
        
        output = ""
        output += "Name: {:} {:}\n".format(self._firstName, self._lastName)
        output += "Birthday: {:} ({:} years old)\n".format(self._birthday, self._age)

        if(self._province is None):
            output += "Birthplace: {:}, {:}\n".format(self._city, self._country)
        else:
            output += "Birthplace: {:}, {:}, {:}\n".format(self._city, self._province, self._country)

        output += "Nationality: {:}\n".format(self._nationality)
        output += "Height: {:}\n".format(self._height)
        output += "Weight: {:}lbs\n".format(self._weight)

        if(self._number is not None):
            output += "Number: {:}\n".format(self._number)

        output += "Position: {:}\n".format(self._position)

        if(self._cap):
            output += "Captain\n"
        elif(self._alt):
            output += "Alternate Captain\n"
        
        if(self._position == "Goalie"):
            output += "Catches: {:}\n".format(self._shoots)
        else:
            output += "Shoots: {:}\n".format(self._shoots)

        


        output += "Team: {:}\n".format(self._team)

        return output

    def get_name(self):
        return "{:} {:}".format(self._firstName, self._lastName)

    def player_info_short(self):
        return "{:},{:} {:},{:}\n".format(self._id, self._firstName.lower(), self._lastName.lower(), self._team.lower())