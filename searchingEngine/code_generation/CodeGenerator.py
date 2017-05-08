import logging
from searchingEngine.models import Actuator
from searchingEngine.code_generation.CodeData import CodeData
from searchingEngine.code_generation.Options import Options
from searchingEngine.code_generation.ActuatorsToMotors import ActuatorsToMotors


class CodeGenerator:

    @staticmethod
    def generate_codes_for_request(request):
        stroke = request['input_data[step]']
        result = {
            "actuator_code_wrappers": [],
            "drive_shaft_options": Options.drive_shaft_options,
            "magnetic_sensors_options": Options.magnetic_sensors_options,
            "profile_mounting_options": Options.profile_mounting_options
        }
        logging.warning("Takie o dostalismy %s" % result)

        actuators_ids = request.getlist("checked_actuators_ids[]")
        for actuators_id in actuators_ids:
            actuator = Actuator.objects.get(id=actuators_id)
            logging.warning(actuators_id)
            logging.warning(actuator)
            result["actuator_code_wrappers"].append(CodeGenerator.generate_for_actuator(actuator, stroke))
        return result


    @staticmethod
    def generate_for_actuator(actuator, stroke):

        actuator_size = 25

        code_data = CodeData()
        code_data.size = actuator_size
        code_data.stroke = stroke
        code_data.mounting_kit = CodeGenerator.choose_mounting_kit(actuator.name)

        return {
            "name": actuator.name,
            "code_data": code_data
        }

    @staticmethod
    def choose_mounting_kit(actuator_name):
        options = ActuatorsToMotors.map[actuator_name]
        motors_options, gears_options = CodeGenerator.split_options(options)
        motor = CodeGenerator.find_motor(motors_options)
        if motor is not None:
            return motor
        motor, gear = CodeGenerator.find_motor_with_gear(gears_options)
        if motor is not None and gear is not None:
            return motor + ", " + gear
        return "pucha2"

    @staticmethod
    def split_options(options):
        motors_options = []
        gears_options = []
        for option in options:
            if isinstance(option, str):
                gears_options.append(option)
            elif isinstance(option, tuple):
                motors_options.append(option)
        return motors_options, gears_options

    @staticmethod
    def find_motor(motors_options):
        return 0

    @staticmethod
    def find_motor_with_gear(gears_options):
        return 0

