import logging
from django.shortcuts import render
from django.http import JsonResponse
from actuatorsSearcher.settings import STATIC_URL
from searchingEngine.models import Actuator, InputData, ActuatorType, ActuatorOrientation, MotionProfileType
from searchingEngine.calculations.Calculator import Calculator
from searchingEngine.code_generation.CodeGenerator import CodeGenerator


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
            ActuatorOrientation.horizontal_bottom.name: 'Horizontal bottom',
            ActuatorOrientation.vertical.name: 'Vertical'
        },
        'motion_profiles': {
            MotionProfileType.acc_and_speed.name: 'acc_and_speed',
            MotionProfileType.total_time.name: 'total_time',
            MotionProfileType.total_and_acc_time.name: 'total_and_acc_time'
        },
        'actuators': []
    }
    return render(request, 'searchingEngine/index.html', context)


def get_actuators(request):
    input_data = get_validated_model_from_request(request)
    actuators = Actuator.objects.all()

    logging.warning("Got input data and actuators list, going to filter actuators")
    results = Calculator.filter_matching_actuators(actuators, input_data)
    get_all_actuators_for_display(results)

    result = {
        'actuators': get_all_actuators_for_display(results)
    }
    return JsonResponse(result)


def get_validated_model_from_request(request):
    logging.warning("get_validated_model_from_request with request %s" % request)
    if not request.GET:
        logging.error("no model provided")
    input_data = InputData.from_request_data(request.GET)
    input_data.log()
    return input_data


def get_all_actuators_for_display(calculations_result):
    result = []
    for actuator, calculation_result in calculations_result.items():
        logging.warning(actuator.name)
        result.append({
            'name': actuator.name,
            'id': actuator.id
        })
    logging.warning(result)
    return result


def get_codes(request):
    logging.warning("got request %s to get_codes" % request.GET)
    context = CodeGenerator.generate_codes_for_request(request.GET)
    logging.warning("get_codes calculated result %s " % context)
    return render(request, 'searchingEngine/codes.html', context)


def send_order(request):
    logging.warning("got request %s to send_order" % request.GET)
    result = {}
    return JsonResponse(result)