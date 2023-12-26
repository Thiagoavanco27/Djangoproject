from django.http import HttpResponse
from django.shortcuts import render

def _home(request):
    return HttpResponse('É natal')

