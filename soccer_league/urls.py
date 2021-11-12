from django.urls import path

from . import views

urlpatterns = [path("test_client", views.test_client, name="test_client")]
