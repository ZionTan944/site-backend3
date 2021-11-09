import json
from django.http import JsonResponse

from .soccer_client.soccer_league_client import SoccerLeagueClient

from .soccer_utils import retrieve_team_from_league

# default initialisation
DEFAULT_LEAGUE = "English Premier League"
# DEFAULT_LEAGUE = "Test League"
# DEFAULT_LEAGUE = "EFL Championship"

soccer_teams, _ = retrieve_team_from_league(DEFAULT_LEAGUE)

soccer_league = SoccerLeagueClient(DEFAULT_LEAGUE, soccer_teams)
# soccer_league.team_lst[2].team_name


def initialise_teams(request):
    league_name = json.loads(request.body).get("league", "")
    if request.method == "POST":
        _, teams = retrieve_team_from_league(league_name)

    return JsonResponse({"data": list(teams.values())})


def test_client(request):
    initialise = json.loads(request.body).get("initialise", "true")
    if initialise == "true":
        soccer_league.reset_season(DEFAULT_LEAGUE, soccer_teams)
        soccer_league.prepare_season()
    soccer_league.run_season()
    return JsonResponse({"data": "none"})
