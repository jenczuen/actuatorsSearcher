import logging
from django.shortcuts import render
from django.http import JsonResponse
from actuatorsSearcher.settings import STATIC_URL
from searchingEngine.models import Actuator, InputData, ActuatorType, ActuatorOrientation, MotionProfileType


def index(request):
    logging.basicConfig()

    context = {
        'static_url': STATIC_URL,
        'actuator_types': {
            ActuatorType.carriage.name: 'Carriage',
            ActuatorType.piston_rod.name: 'Piston rod',
            ActuatorType.pion.name: 'PION'
        },
        'actuator_orientations': {
            ActuatorOrientation.horizontal_top.name: 'Horizontal top',
            ActuatorOrientation.horizontal_side.name: 'Horizontal side',
            ActuatorOrientation.horizontal_bottom.name: 'Horizontal side',
            ActuatorOrientation.vertical.name: 'Vertical'
        },
        'motion_profiles': {
            MotionProfileType.acc_and_speed.name: 'acc_and_speed',
            MotionProfileType.total_time.name: 'total_time',
            MotionProfileType.total_and_acc_time.name: 'total_and_acc_time'
        },
        'actuators': Actuator.objects.all()
    }
    return render(request, 'searchingEngine/index.html', context)


def filter_actuators(request):
    get_validated_model_from_request(request)
    result = {
        'actuators': Actuator.get_all_actuators_for_display()
    }
    return JsonResponse(result)


def get_validated_model_from_request(request):
    if not request.GET:
        logging.error("no model provided")
    input_data = InputData.from_request_data(request.GET)
    input_data.log()

