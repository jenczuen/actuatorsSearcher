from searchingEngine.validation.Validator import Validator
from searchingEngine.models import MotionProfileType
from searchingEngine.models import ActuatorOrientation
from math import pi


class Calculator:
    def __init__(self, actuator, input_data):
        self.validator = Validator(actuator)
        self.actuator = actuator
        self.input_data = input_data
        self.validator.validate_max_stroke(input_data.stroke)
        self.g = 9.807

    def calculate_result(self):
        """
        input_data.actuator_type ????????????
        """

        a_max, V_max = AccAndSpeedCalculator.calculate(self.input_data)
        self.validator.validate_Vmax(V_max)
        self.validator.validate_a(a_max)

        F_a, F = self._calculate_forces(a_max)
        return SingleResult(
            torque=self._calculate_torque(F, F_a, V_max),
            sum_of_combined_load=0,
            torque_load=0,
            errors=self.validator.log_list
        )

    def _calculate_forces(self, a):
        m_total = self.input_data.mass + self.actuator.carriage_mass
        F_0 = self.actuator.no_load_torque * 2 * pi / self.actuator.pulley_circumference_mm
        F_a = m_total * a
        if self.input_data.actuator_orientation == ActuatorOrientation.horizontal_top or \
                self.input_data.actuator_orientation == ActuatorOrientation.horizontal_bottom or \
                self.input_data.actuator_orientation == ActuatorOrientation.horizontal_side:
            return F_a, F_a + F_0
        else:
            return F_a, F_a + F_0 + self.g * m_total

    def _calculate_torque(self, F, F_a, V_max):
        self.validator.validate_Fa(F_a, V_max)
        self.validator.validate_Mz(self.input_data.distance_of_mass_y * F_a) # M_z

        if self.input_data.distance_of_mass_z > 0:
            self.validator.validate_My(self.input_data.distance_of_mass_z * F_a) # M_y

        r = self.actuator.pulley_circumference_mm / (2*pi)
        return F * r


class AccAndSpeedCalculator:

    @classmethod
    def calculate(cls, input_data):
        if input_data.motion_profile.type is MotionProfileType.acc_and_speed:
            return cls.calculate_for_type_1(input_data)

        if input_data.motion_profile.type is MotionProfileType.total_time:
            return cls.calculate_for_type_2(input_data)

        if input_data.motion_profile.type is MotionProfileType.total_and_acc_time:
            return cls.calculate_for_type_3(input_data)


    @staticmethod
    def calculate_for_type_1(input_data):
        return input_data.motion_profile.v_max, input_data.motion_profile.acc

    @staticmethod
    def calculate_for_type_2(input_data):
        t = input_data.motion_profile.t_total / 2
        a_max = input_data.stroke / (t * t)
        V_max = a_max * input_data.motion_profile.t_total / 2
        return a_max, V_max

    @staticmethod
    def calculate_for_type_3(input_data):
        V_max = 2 * input_data.stroke / \
                (input_data.motion_profile.t_total - input_data.motion_profile.t_acc_dcc)
        a_max = V_max / input_data.motion_profile.t_acc_dcc
        return a_max, V_max


class SingleResult:
    def __init__(self, torque, sum_of_combined_load, torque_load, errors=None):
        self.torque = torque
        self.sum_of_combined_load = sum_of_combined_load
        self.torque_load = torque_load
        self.errors = errors

    def passed_validation(self):
        return self.errors is None or len(self.errors) == 0
