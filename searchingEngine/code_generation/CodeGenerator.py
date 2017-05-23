import logging
from searchingEngine.models import Actuator
from searchingEngine.code_generation.CodeData import CodeData
from searchingEngine.code_generation.Options import Options
from searchingEngine.code_generation.MotorsMatcher import MotorsMatcher


class CodeGenerator:

    @staticmethod
    def generate_codes_for_request(request):
        myDict = request.dict()
        logging.warning("myDict = %s" % myDict)

        stroke = request['input_data[step]']
        result = {
            "actuator_code_wrappers": [],
            "drive_shaft_options": Options.drive_shaft_options,
            "magnetic_sensors_options": Options.magnetic_sensors_options,
            "profile_mounting_options": Options.profile_mounting_options
        }
        logging.warning("Takie o dostalismy %s" % result)

        calculated_torque = request['calculated_data[torque]']
        calculated_speed = request['calculated_data[speed]']
        logging.warning("calculated_torque = %s, calculated_speed = %s"
                        % (calculated_torque, calculated_speed))

        actuators_ids = request.getlist("checked_actuators_ids[]")
        for actuators_id in actuators_ids:
            actuator = Actuator.objects.get(id=actuators_id)
            logging.warning(actuators_id)
            logging.warning(actuator)
            result["actuator_code_wrappers"].append(CodeGenerator.generate_for_actuator(actuator, stroke, calculated_torque, calculated_speed))
        return result


    @staticmethod
    def generate_for_actuator(actuator, stroke, calculated_torque, calculated_speed):
        # ------------ !!!!!111one11
        actuator_size = 25
        # ------------ !!!!!111one11

        code_data = CodeData()
        code_data.size = actuator_size
        code_data.stroke = stroke
        code_data.mounting_kit = MotorsMatcher.choose_mounting_kit(
            actuator_name=actuator.name,
            torque=calculated_torque,
            speed=calculated_speed,
            circumference_mm=actuator.pulley_circumference_mm,
        )

        return {
            "name": actuator.name,
            "code_data": code_data
        }



