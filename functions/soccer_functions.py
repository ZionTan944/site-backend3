import json

from soccer_league.models import SoccerTeam, SoccerLeague
from client.soccer_client.soccer_team_client import SoccerTeamClient


def retrieve_team_from_league(league_name):
    league = SoccerLeague.objects.get(league_name=league_name)
    teams = SoccerTeam.objects.filter(team_league=league).order_by("team_rate")

    team_class_list = []
    index = 1
    for team in teams:
        team_class_list.append(
            SoccerTeamClient(team.team_name, team.team_int, team.team_rate, index)
        )
        index += 1

    return json.loads(league.meta_json), team_class_list
