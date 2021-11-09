from django.contrib import admin
from .models import SoccerLeague, SoccerTeam


@admin.register(SoccerLeague)
class SoccerLeagueAdmin(admin.ModelAdmin):
    list_display = ("id", "league_name")


@admin.register(SoccerTeam)
class SoccerTeamAdmin(admin.ModelAdmin):
    list_display = ("id", "team_name", "team_rate", "team_league")
    list_filter = ["team_league"]
