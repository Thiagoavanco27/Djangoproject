from django.urls import path

from . import views

app_name = "philosophies"

urlpatterns = [
    path("", views.home, name="Home"),
    path("meditations/<int:id>/", views.meditation, name="Meditation"),
]
