import logging
from django.shortcuts import render
from .models import Actuator

logger = logging.getLogger(__name__)


def index(request):
    logging.basicConfig()
    actuators = Actuator.objects.all()
    context = {
        'actuator_types': [
            'karetka',
            'tloczysko',
            'pion'
        ],
        'actuator_orientations': [
            'horizontal_top',
            'horizontal_side',
            'vertical'
        ],
        'motion_profiles': [
            'acc_and_speed',
            'total_time',
            'total_time_and_acc'
        ],
        'actuators': actuators
    }
    return render(request, 'searchingEngine/index.html', context)


