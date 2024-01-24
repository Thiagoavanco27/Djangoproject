from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("meditations/<int:id>/", views.meditation, name="Meditation"),
]
