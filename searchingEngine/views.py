import logging
from django.shortcuts import render
from django.http import JsonResponse
from .models import Actuator

def index(request):
    logging.basicConfig()
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
        'actuators': Actuator.objects.all()
    }
    return render(request, 'searchingEngine/index.html', context)


def filter_actuators(request):
    model = request.GET
    logging.warning(model['model'])
    result = {
        'actuators': Actuator.get_all_actuators_for_display()
    }
    return JsonResponse(result)
