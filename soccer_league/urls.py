from django.urls import path

from . import views

urlpatterns = [
    path("init_team", views.initialise_teams, name="init_team"),
    path("test_client", views.test_client, name="test_client"),
]
