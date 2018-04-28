from django.shortcuts import render


def index(request):
    context = {'auth': True}
    return render(request, 'index.html', context)



