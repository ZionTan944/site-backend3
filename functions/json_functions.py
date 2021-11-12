import json

# Data to be written
TeamName = [
    "Chelsea",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Everton",
    "Brighton",
    "Brentford",
    "Tottenhem",
    "West Ham United",
    "Aston Villa",
    "Arsenal",
    "Wolves",
    "Leicester City",
    "Crystal Palace",
    "Watford",
    "Leeds United",
    "Southampton",
    "Burnley",
    "Newcastle",
    "Norwich City",
]
TeamInt = [
    "CHE",
    "LIV",
    "MCI",
    "MUN",
    "EVE",
    "BHA",
    "BRE",
    "TOT",
    "WHU",
    "AVL",
    "ARS",
    "WOL",
    "LEI",
    "CRY",
    "WAT",
    "LEE",
    "SOU",
    "BUR",
    "NEW",
    "NOR",
]
TeamRate = [
    390,
    380,
    370,
    320,
    300,
    220,
    220,
    300,
    210,
    180,
    290,
    160,
    150,
    140,
    130,
    120,
    110,
    90,
    70,
    50,
]


def create_soccer_league_json_object(
    league_name, team_name_list, team_int_list, team_rate_list
):
    json_object = {"league": "", "teams": []}
    if len(team_name_list) != len(team_int_list) != len(team_rate_list):
        return json_object

    json_object["league"] = league_name
    for index in range(len(team_name_list)):
        json_object["teams"].append(
            {
                "name": team_name_list[index],
                "int": team_int_list[index],
                "rate": team_rate_list[index],
            }
        )
    return json_object


def write_json_file(file, json_object):
    dumped_object = json.dumps(json_object, indent=4)
    with open(file, "w") as outfile:
        outfile.write(dumped_object)


def read_json_file(file):
    with open(file, "r") as readfile:
        json_object = json.loads(readfile.read())

    return json_object


if __name__ == "__main__":
    json_object = create_soccer_league_json_object(
        "English Premier League", TeamName, TeamInt, TeamRate
    )
    write_json_file("./data.json", json_object)
