from django.shortcuts import render


def index(request):
    context = {'auth': True}
    return render(request, 'index.html', context)


def leaflet(request):
    context = {'auth': True}
    return render(request, 'leaflet.html', context)


def analysis(request):
    context = {'auth': True}
    return render(request, 'analysis.html', context)

