import json
from django.http import JsonResponse

from client.soccer_client.soccer_league_client import SoccerLeagueClient

from functions.soccer_functions import retrieve_team_from_league

# default initialisation
DEFAULT_LEAGUE = "English Premier League"
# DEFAULT_LEAGUE = "EFL Championship"


def test_client(request):
    initialise = json.loads(request.body).get("initialise", "true")
    if initialise == "true":
        league_json, soccer_teams = retrieve_team_from_league(DEFAULT_LEAGUE)
        soccer_league = SoccerLeagueClient(DEFAULT_LEAGUE, league_json, soccer_teams)
        soccer_league.reset_season(soccer_teams)
        soccer_league.prepare_season()
    soccer_league.run_season()
    return JsonResponse({"data": "none"})
