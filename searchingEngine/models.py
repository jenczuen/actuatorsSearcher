import logging
from django.db import models
from enum import Enum


class Actuator(models.Model):
    name = models.CharField(max_length=25)
    carriage_mass = models.FloatField()
    no_load_torque = models.FloatField()
    pulley_circumference_mm = models.IntegerField()
    max_applied_load_Fy = models.IntegerField()
    max_applied_load_Fz = models.IntegerField()
    max_moment_Mx = models.FloatField()
    max_moment_My = models.FloatField()
    max_moment_Mz = models.FloatField()
    max_stroke_mm = models.IntegerField()
    max_speed = models.FloatField()
    max_acc = models.FloatField()
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
        return result


class InputData:
    def __init__(self, **kwargs):
        self.stroke = 0
        self.mass = 0
        self.actuator_type = None
        self.actuator_orientation = None
        self.distance_of_mass_x = 0
        self.distance_of_mass_y = 0
        self.distance_of_mass_z = 0
        self.motion_profile = None
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @staticmethod
    def from_request_data(request_data):
        return InputData(
            stroke=Helper.parse_int(request_data['step']),
            mass=Helper.parse_float(request_data['mass']),
            actuator_type=ActuatorType[request_data['actuator_type']],
            actuator_orientation=ActuatorOrientation[request_data['actuator_orientation']],
            distance_of_mass_x=Helper.parse_int(request_data['distance_of_mass_x']),
            distance_of_mass_y=Helper.parse_int(request_data['distance_of_mass_y']),
            distance_of_mass_z=Helper.parse_int(request_data['distance_of_mass_z']),
            motion_profile=MotionProfileFactory.from_request_data(request_data)
        )

    def log(self):
        logging.warning("stroke = %s" % self.stroke)
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
    horizontal_side = 2
    vertical = 3


class MotionProfileFactory:
    @staticmethod
    def from_request_data(request_data):
        motion_profile_type = MotionProfileType[request_data['motion_profile']]

        if motion_profile_type is MotionProfileType.acc_and_speed:
            return MotionProfile_AccAndSpeed.from_request_data(request_data)

        if motion_profile_type is MotionProfileType.total_time:
            return MotionProfile_TotalTime.from_request_data(request_data)

        if motion_profile_type is MotionProfileType.total_and_acc_time:
            return MotionProfile_TotalAndAccTime.from_request_data(request_data)


class MotionProfileType(Enum):
    acc_and_speed = 0
    total_time = 1
    total_and_acc_time = 2


class MotionProfile_AccAndSpeed:
    def __init__(self, **kwargs):
        self.type = MotionProfileType.acc_and_speed
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @staticmethod
    def from_request_data(request_data):
        return MotionProfile_AccAndSpeed(
            v_max=Helper.parse_float(request_data['motion_profile_params[v_max]']),
            acc=Helper.parse_float(request_data['motion_profile_params[acc]'])
        )

    def log(self):
        logging.warning("type = %s" % self.type)
        logging.warning("v_max = %s" % self.v_max)
        logging.warning("acc = %s" % self.acc)


class MotionProfile_TotalTime:
    def __init__(self, **kwargs):
        self.type = MotionProfileType.total_time
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @staticmethod
    def from_request_data(request_data):
        return MotionProfile_TotalTime(
            t_total=Helper.parse_float(request_data['motion_profile_params[t_total]'])
        )

    def log(self):
        logging.warning("type = %s" % self.type)
        logging.warning("t_total = %s" % self.t_total)


class MotionProfile_TotalAndAccTime:
    def __init__(self, **kwargs):
        self.type = MotionProfileType.total_and_acc_time
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @staticmethod
    def from_request_data(request_data):
        return MotionProfile_TotalAndAccTime(
            t_total=Helper.parse_float(request_data['motion_profile_params[t_total]']),
            t_acc_dcc=Helper.parse_float(request_data['motion_profile_params[t_acc_dcc]'])
        )

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
