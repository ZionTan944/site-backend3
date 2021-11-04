from django.urls import path

from . import views

urlpatterns = [path("init_team", views.initialise_teams, name="init_team")]
