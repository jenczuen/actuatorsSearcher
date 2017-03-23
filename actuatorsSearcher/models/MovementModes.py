from Actuator import CarriagePosition
from math import pi

class MovementModeBase:
    def __init__(self):
        self.g = 9.807

    def setInput(self, step, I_x, I_y, I_z, m, carriage_position, M_0, circ, m_carriage):
        self.step = step
        self.I_x = I_x
        self.I_y = I_y
        self.I_z = I_z
        self.m = m
        self.carriage_position = carriage_position
        self.M_0 = M_0 #z katalogu
        self.circ = circ #obwod z katalogu
        self.m_carriage = m_carriage #z katalogu

    def _calculate_force(self, a):
        m_total = self.m + self.m_carriage
        F_0 = self.M_0 * 2 * pi / self.circ
        F_a = m_total * a
        if self.carriage_position == CarriagePosition.HORIZONTAL_TOP or \
                self.carriage_position == CarriagePosition.HORIZONTAL_BOTTOM or \
                self.carriage_position == CarriagePosition.HORIZONTAL_SIDE:
            return F_a, F_a + F_0
        else:
            return F_a, F_a + F_0 + self.g * m_total

    def _check_force(self, F, F_a, V_max):
        if V_max <= 1:
            pass  # F z kolumna G
        elif V_max <= 3:
            pass  # F z kolumna H
        else:
            pass  # F z kolumna I

        M_z = self.I_y * F_a  # kolumna E
        if self.I_z > 0:
            M_y = self.I_z * F_a  # kolumna F

        r = self.circ / (2*pi)
        return F * r


class MovementParams1(MovementModeBase):
    def __init__(self, V_max, a_max):
        MovementModeBase.__init__(self)
        self.V_max = V_max  # ograniczone kolumna J
        self.a_max = a_max  # ograniczone kolumna K

    def check(self):
        F_a, F = self._calculate_force(self.a_max)
        return self._check_force(F, F_a, self.V_max)


class MovementParams2(MovementModeBase):
    def __init__(self, t_total):
        MovementModeBase.__init__(self)
        self.t_total = t_total

    def __calculate_max_acc_speed(self):
        t = self.t_total / 2
        a_max = self.step / (t*t)
        V_max = a_max * self.t_total / 2
        return a_max, V_max

    def check(self):
        a_max, V_max = self.__calculate_max_acc_speed()
        F_a, F = self._calculate_force(a_max)
        return self._check_force(F, F_a, V_max)


class MovementParams3(MovementModeBase):
    def __init__(self, t_total, t_acc_dcc):
        MovementModeBase.__init__(self)
        self.t_total = t_total
        self.t_acc_dcc = t_acc_dcc

    def __calculate_max_acc_speed(self):
        V_max = 2 * self.step / (self.t_total - self.t_acc_dcc)
        a_max = V_max / self.t_acc_dcc
        return a_max, V_max

    def check(self):
        a_max, V_max = self.__calculate_max_acc_speed()
        F_a, F = self._calculate_force(a_max)
        return self._check_force(F, F_a, V_max)