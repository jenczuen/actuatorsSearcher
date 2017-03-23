from django.conf import settings
from Actuator import CarriagePosition
from MovementModes import MovementParams1

#dane
#m = 5kg, step = 1000mm, I_y = 50mm, a_max = 5, V_max = 5, Carriage horizontal top
#M = 2.385, 7%

class ActuatorTests():
    def setUp(self):
        self.m = 5  # kg
        self.step  = 1    # 1000 mm
        self.I_y   = 0.05 #   50 mm
        self.a_max = 5  # m/s2
        self.V_max = 5  # m/s
        self.carriage_position = CarriagePosition.HORIZONTAL_TOP

        self.expected_M = 2.385

        # OSPE-BHD1-25
        self.data = {
            "A":   6700,
            "B": 	3000,
            "C": 	2000,
            "D": 	50,
            "E": 	500,
            "F": 	500,
            "J": 	5,
            "K": 	50,
            "circ": 0.180,
            "m_carriage": 1.5,
            "M_0": 1.2
        }

    def atest_calculations(self):
        mp = MovementParams1(
            a_max = self.a_max,
            V_max = self.V_max
        )
        mp.setInput(
            m = self.m,
            I_x = 0,
            I_y = self.I_y,
            I_z = 0,
            step = self.step,
            carriage_position = self.carriage_position,
            circ = self.data['circ'],
            m_carriage = self.data['m_carriage'],
            M_0 = self.data['M_0']
        )
        return mp.check()

a = ActuatorTests()
a.setUp()
calculated_M = a.atest_calculations()
print("calculated_M = %s\nexpected_M   = %s" % (calculated_M, a.expected_M))
