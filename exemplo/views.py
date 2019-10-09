from django.shortcuts import render

from .models import Slide, Card


def index(request):
    context = {
        'slides': Slide.objects.all(),
        'cards': Card.objects.all(),
    }
    return render(request, 'index.html', context)