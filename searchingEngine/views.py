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

    model = request.GET
    logging.warning(model['expected_step'])
    logging.warning(model['actuator_type'])
    logging.warning(model['actuator_orientation'])
    logging.warning(model['distance_of_mass_y'])
    logging.warning(model['distance_of_mass_x'])
    logging.warning(model['distance_of_mass_z'])
    logging.warning(model['motion_profile'])
    logging.warning(model['motion_profile_params[t_total]'])
    logging.warning(model['motion_profile_params[acc_dcc]'])

