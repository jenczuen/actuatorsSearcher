import logging
from django.db import models
from enum import Enum


class Actuator(models.Model):
    name = models.CharField(max_length=20)
    carriage_mass = models.FloatField()
    no_load_torque = models.FloatField()
    pulley_circumference_mm = models.IntegerField()
    max_applied_load_Fy = models.IntegerField()
    max_applied_load_Fz = models.IntegerField()
    max_moment_Mx = models.IntegerField()
    max_moment_My = models.IntegerField()
    max_moment_Mz = models.IntegerField()
    max_stroke_mm = models.IntegerField()
    max_speed = models.IntegerField()
    max_acc = models.IntegerField()
    max_effective_action_force_1 = models.IntegerField()
    max_effective_action_force_2 = models.IntegerField()
    max_effective_action_force_3 = models.IntegerField()
    max_effective_action_force_border_1 = models.IntegerField()
    max_effective_action_force_border_2 = models.IntegerField()

    @staticmethod
    def get_all_actuators_for_display():
        result = []
        for a in Actuator.objects.all():
            result.append({
                'name': a.name
            })
        result.append({'name': 'dummy1'})
        result.append({'name': 'dummy2'})
        return result


class InputData:
    def __init__(self):
        self.stroke = 0
        self.mass = 0
        self.actuator_type = None
        self.actuator_orientation = None
        self.distance_of_mass_x = 0
        self.distance_of_mass_y = 0
        self.distance_of_mass_z = 0
        self.motion_profile = None

    @staticmethod
    def from_request_data(request_data):
        input_data = InputData()

        input_data.stroke = Helper.parse_int(request_data['step'])
        input_data.mass = Helper.parse_float(request_data['mass'])

        input_data.actuator_type = ActuatorType[request_data['actuator_type']]
        input_data.actuator_orientation = ActuatorOrientation[request_data['actuator_orientation']]

        input_data.distance_of_mass_x = Helper.parse_int(request_data['distance_of_mass_x'])
        input_data.distance_of_mass_y = Helper.parse_int(request_data['distance_of_mass_y'])
        input_data.distance_of_mass_z = Helper.parse_int(request_data['distance_of_mass_z'])

        input_data.motion_profile = MotionProfileFactory.from_request_data(request_data)
        return input_data

    def log(self):
        logging.warning("step = %s" % self.step)
        logging.warning("mass = %s" % self.mass)
        logging.warning("actuator_type = %s" % self.actuator_type)
        logging.warning("actuator_orientation = %s" % self.actuator_orientation)
        logging.warning("distance_of_mass_x = %s" % self.distance_of_mass_x)
        logging.warning("distance_of_mass_y = %s" % self.distance_of_mass_y)
        logging.warning("distance_of_mass_z = %s" % self.distance_of_mass_z)
        self.motion_profile.log()


class ActuatorType(Enum):
    carriage = 0
    piston_rod = 1
    pion = 2


class ActuatorOrientation(Enum):
    horizontal_top = 0
    horizontal_bottom = 1
    horizontal_side = 1
    vertical = 2


class MotionProfileFactory:
    @staticmethod
    def from_request_data(request_data):
        motion_profile_type = MotionProfileType[request_data['motion_profile']]

        if motion_profile_type is MotionProfileType.acc_and_speed:
            return MotionProfile1.from_request_data(request_data)

        if motion_profile_type is MotionProfileType.total_time:
            return MotionProfile2.from_request_data(request_data)

        if motion_profile_type is MotionProfileType.total_and_acc_time:
            return MotionProfile3.from_request_data(request_data)


class MotionProfileType(Enum):
    acc_and_speed = 0
    total_time = 1
    total_and_acc_time = 2


class MotionProfile1:
    def __init__(self):
        self.type = MotionProfileType.acc_and_speed

    @staticmethod
    def from_request_data(request_data):
        result = MotionProfile1()
        result.v_max = Helper.parse_float(request_data['motion_profile_params[v_max]'])
        result.acc = Helper.parse_float(request_data['motion_profile_params[acc]'])
        return result

    def log(self):
        logging.warning("type = %s" % self.type)
        logging.warning("v_max = %s" % self.v_max)
        logging.warning("acc = %s" % self.acc)


class MotionProfile2:
    def __init__(self):
        self.type = MotionProfileType.total_time

    @staticmethod
    def from_request_data(request_data):
        result = MotionProfile2()
        result.t_total = Helper.parse_int(request_data['motion_profile_params[t_total]'])
        return result

    def log(self):
        logging.warning("type = %s" % self.type)
        logging.warning("t_total = %s" % self.t_total)


class MotionProfile3:
    def __init__(self):
        self.type = MotionProfileType.total_and_acc_time

    @staticmethod
    def from_request_data(request_data):
        result = MotionProfile3()
        result.t_total = Helper.parse_int(request_data['motion_profile_params[t_total]'])
        result.t_acc_dcc = Helper.parse_int(request_data['motion_profile_params[t_acc_dcc]'])
        return result

    def log(self):
        logging.warning("type = %s" % self.type)
        logging.warning("t_total = %s" % self.t_total)
        logging.warning("t_acc_dcc = %s" % self.t_acc_dcc)


class Helper:
    @staticmethod
    def parse_int(input_number):
        if input_number == "":
            return int(0)
        else:
            return int(input_number)

    @staticmethod
    def parse_float(input_number):
        if input_number == "":
            return float(0)
        else:
            return float(input_number)
