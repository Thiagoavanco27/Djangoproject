from django.shortcuts import render


def home(request):
    return render(request, 'templates/philosophia/pages/index.html')
