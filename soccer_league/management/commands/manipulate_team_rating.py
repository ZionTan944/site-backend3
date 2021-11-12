from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count, F, Value

from soccer_league.models import SoccerLeague, SoccerTeam


class Command(BaseCommand):
    def handle(self, *args, **options):
        league_name = "English Premier League"
        league = SoccerLeague.objects.get(league_name=league_name)
        SoccerTeam.objects.filter(team_league=league).update(
            team_rate=F("team_rate") * 4
        )
