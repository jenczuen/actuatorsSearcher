from actuatorsSearcher.models.Actuator import CarriagePosition
from searchingEngine.validation.Validator import Validator
from searchingEngine.models import MotionProfileType
from math import pi


class Calculator:
    def __init__(self, actuator):
        self.actuator = actuator
        self.validator = Validator(actuator)
        self.g = 9.807

    def set_input_data(self, input_data):
        self.input_data = input_data
        self.validator.validateColumnA(input_data.step)

    def calculate_torque(self):
        a_max, V_max = AccAndSpeedCalculator.calculate(self.input_data)
        self.validator.validateColumnJ(V_max)
        self.validator.validateColumnK(a_max)

        F_a, F = self._calculate_forces(a_max)
        return self._calculate_torque(F, F_a, V_max)

    def _calculate_forces(self, a):
        m_total = self.input_data.m + self.actuator.m_carriage
        F_0 = self.actuator.M_0 * 2 * pi / self.actuator.circ
        F_a = m_total * a
        if self.input_data.carriage_position == CarriagePosition.HORIZONTAL_TOP or \
                self.input_data.carriage_position == CarriagePosition.HORIZONTAL_BOTTOM or \
                self.input_data.carriage_position == CarriagePosition.HORIZONTAL_SIDE:
            return F_a, F_a + F_0
        else:
            return F_a, F_a + F_0 + self.g * m_total

    def _calculate_torque(self, F, F_a, V_max):
        if V_max <= 1:
            self.validator.validateColumnG(F)
        elif V_max <= 3:
            self.validator.validateColumnH(F)
        else:
            self.validator.validateColumnI(F)

        self.validator.validateColumnE(self.input_data.I_y * F_a) # M_z

        if self.input_data.I_z > 0:
            self.validator.validateColumnF(self.input_data.I_z * F_a) # M_y

        r = self.actuator.circ / (2*pi)
        return F * r


class AccAndSpeedCalculator:

    @classmethod
    def calculate(cls, input_data):
        if input_data.motion_profile is MotionProfileType.acc_and_speed:
            return cls.calculate_for_type_1(input_data)

        if input_data.motion_profile is MotionProfileType.total_time:
            return cls.calculate_for_type_2(input_data)

        if input_data.motion_profile is MotionProfileType.total_and_acc_time:
            return cls.calculate_for_type_3(input_data)


    @staticmethod
    def calculate_for_type_1(input_data):
        return input_data.motion_profile.V_max, input_data.motion_profile.a_max

    @staticmethod
    def calculate_for_type_2(input_data):
        t = input_data.motion_profile.t_total / 2
        a_max = input_data.motion_profile.input_data.step / (t * t)
        V_max = a_max * input_data.motion_profile.t_total / 2
        return a_max, V_max

    @staticmethod
    def calculate_for_type_3(input_data):
        V_max = 2 * input_data.motion_profile.step / \
                (input_data.motion_profile.t_total - input_data.motion_profile.t_acc_dcc)
        a_max = V_max / input_data.motion_profile.t_acc_dcc
        return a_max, V_max