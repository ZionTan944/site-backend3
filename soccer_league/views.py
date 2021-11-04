import json
from django.http import JsonResponse

from .models import SoccerTeam, SoccerLeague


def initialise_teams(request):
    league_name = json.loads(request.body).get("league", "")
    if request.method == "POST":
        league = SoccerLeague.objects.get(league_name=league_name)
        teams = SoccerTeam.objects.filter(team_league=league)

    return JsonResponse({"data": list(teams.values())})
