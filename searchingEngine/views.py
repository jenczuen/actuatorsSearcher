import logging
from django.shortcuts import render
from .models import Actuator

logger = logging.getLogger(__name__)


def index(request):
    logging.basicConfig()
    actuators = Actuator.objects.all()
    logging.info("---------------------------- witam")
    logging.info(actuators)
    context = {'actuators': actuators}
    return render(request, 'searchingEngine/index.html', context)