from django.shortcuts import render


def home(request):
    return render(request, 'philosofia/pages/index.html', context={
        'name': 'Thiago Reis',
    })

def meditation(request, id):
    return render(request, 'philosofia/pages/index.html', context={
        'name': 'Thiago Reis',
    })