from django.urls import path

from . import views

app_name = "philosophies"

urlpatterns = [
    path("", views.home, name="Home"),
    path("meditations/<id>/", views.meditation, name="meditation")
]
