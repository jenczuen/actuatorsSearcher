import logging
from django.shortcuts import render
from .models import Actuator

logger = logging.getLogger(__name__)


def index(request):
    logging.basicConfig()
    actuators = Actuator.objects.all()
    context = {
        'title' : 'Wyszukiwanie to nasza pasja',
        'actuators': actuators
    }
    return render(request, 'searchingEngine/index.html', context)