from django.db import models

# Create your models here.


class SoccerLeague(models.Model):
    id = models.IntegerField(primary_key=True)
    league_name = models.CharField(max_length=200, blank=False)


class SoccerTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=200, blank=False)
    team_int = models.CharField(max_length=4, blank=False)
    team_rate = models.IntegerField(blank=False)
    team_league = models.ForeignKey(SoccerLeague, on_delete=models.CASCADE)
