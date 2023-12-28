from django.urls import path
from philosofia.views import home


urlpatterns = [
    path("", home),
]
