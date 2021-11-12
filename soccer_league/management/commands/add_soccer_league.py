import json

from django.core.management.base import BaseCommand, CommandError
from soccer_league.models import SoccerLeague, SoccerTeam
from functions.json_functions import read_json_file


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = read_json_file("soccer_league/management/data/epl.json")

        league, _ = SoccerLeague.objects.get_or_create(
            league_name=data["league"]["name"],
            meta_json=json.dumps(data["league"]["meta_json"]),
        )

        for team in data["teams"]:
            SoccerTeam.objects.get_or_create(
                team_name=team["name"],
                team_rate=team["rate"],
                team_int=team["int"],
                team_league=league,
            )
