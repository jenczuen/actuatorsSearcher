import logging
from django.shortcuts import render
from django.http import JsonResponse
from actuatorsSearcher.settings import STATIC_URL
from .models import Actuator
from .models import InputData


def index(request):
    logging.basicConfig()
    context = {
        'static_url': STATIC_URL,
        'actuator_types': [
            'carriage',
            'piston_rod',
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
            'total_and_acc_time'
        ],
        'actuators': Actuator.objects.all()
    }
    return render(request, 'searchingEngine/index.html', context)


def filter_actuators(request):
    get_and_validate_model_from_request(request)
    result = {
        'actuators': Actuator.get_all_actuators_for_display()
    }
    return JsonResponse(result)


def get_and_validate_model_from_request(request):
    if not request.GET:
        logging.error("no model provided")
    input_data = InputData.from_request_data(request.GET)
    input_data.log()

