from actuatorsSearcher.models.Actuator import CarriagePosition
from searchingEngine.validation.Validator import Validator
from math import pi

class MovementModeBase:
    def __init__(self, actuator):
        self.actuator = actuator
        self.validator = Validator(actuator)
        self.g = 9.807

    def setInputData(self, step, I_x, I_y, I_z, m, carriage_position):
        self.step = step
        self.I_x = I_x
        self.I_y = I_y
        self.I_z = I_z
        self.m = m
        self.carriage_position = carriage_position

    def _calculate_forces(self, a):
        m_total = self.m + self.actuator.m_carriage
        F_0 = self.actuator.M_0 * 2 * pi / self.actuator.circ
        F_a = m_total * a
        if self.carriage_position == CarriagePosition.HORIZONTAL_TOP or \
                self.carriage_position == CarriagePosition.HORIZONTAL_BOTTOM or \
                self.carriage_position == CarriagePosition.HORIZONTAL_SIDE:
            return F_a, F_a + F_0
        else:
            return F_a, F_a + F_0 + self.g * m_total

    def _calculate_torgue(self, F, F_a, V_max):
        if V_max <= 1:
            self.validator.validateColumnG(F)
        elif V_max <= 3:
            self.validator.validateColumnH(F)
        else:
            self.validator.validateColumnI(F)

        self.validator.validateColumnE(self.I_y * F_a) # M_z

        if self.I_z > 0:
            self.validator.validateColumnF(self.I_z * F_a) # M_y

        r = self.actuator.circ / (2*pi)
        return F * r


class MovementParams1(MovementModeBase):
    def __init__(self, actuator, V_max, a_max):
        MovementModeBase.__init__(self, actuator)

        self.V_max = V_max
        self.validator.validateColumnJ(V_max)

        self.a_max = a_max
        self.validator.validateColumnK(a_max)

    def calculate_torgue(self):
        F_a, F = self._calculate_forces(self.a_max)
        return self._calculate_torgue(F, F_a, self.V_max)


class MovementParams2(MovementModeBase):
    def __init__(self, actuator, t_total):
        MovementModeBase.__init__(self, actuator)
        self.t_total = t_total

    def __calculate_max_acc_speed(self):
        t = self.t_total / 2
        a_max = self.step / (t*t)
        V_max = a_max * self.t_total / 2
        return a_max, V_max

    def calculate_torgue(self):
        a_max, V_max = self.__calculate_max_acc_speed()
        F_a, F = self._calculate_forces(a_max)
        return self._calculate_torgue(F, F_a, V_max)


class MovementParams3(MovementModeBase):
    def __init__(self, actuator, t_total, t_acc_dcc):
        MovementModeBase.__init__(self, actuator)
        self.t_total = t_total
        self.t_acc_dcc = t_acc_dcc

    def __calculate_max_acc_speed(self):
        V_max = 2 * self.step / (self.t_total - self.t_acc_dcc)
        a_max = V_max / self.t_acc_dcc
        return a_max, V_max

    def calculate_torgue(self):
        a_max, V_max = self.__calculate_max_acc_speed()
        F_a, F = self._calculate_forces(a_max)
        return self._calculate_torgue(F, F_a, V_max)