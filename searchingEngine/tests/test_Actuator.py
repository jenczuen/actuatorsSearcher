from django.test import TestCase
from searchingEngine.models import Actuator
from searchingEngine.models import InputData
from searchingEngine.models import ActuatorOrientation
from searchingEngine.models import MotionProfile1
from actuatorsSearcher.models.Calculator import Calculator


class ActuatorTests(TestCase):

    def setUp(self):
        self.input_data = InputData()
        self.input_data.stroke = 1000    # 1000 mm
        self.input_data.mass = 5  # kg
        self.input_data.distance_of_mass_y = 0.05 #   50 mm
        self.input_data.actuator_orientation = ActuatorOrientation.horizontal_top
        self.input_data.motion_profile = MotionProfile1()
        self.input_data.motion_profile.v_max = 5  # m/s
        self.input_data.motion_profile.acc = 5  # m/s2

        self.actuator = Actuator(
            name="ospe-50-b",
            carriage_mass=1,
            no_load_torque=0.6,
            pulley_circumference_mm=100,
            max_applied_load_Fy=0,
            max_applied_load_Fz=850,
            max_moment_Mx=16,
            max_moment_My=80,
            max_moment_Mz=32,
            max_stroke_mm=5000,
            max_speed=5,
            max_acc=10,
            max_effective_action_force_1=425,
            max_effective_action_force_2=375,
            max_effective_action_force_3=300,
            max_effective_action_force_border_1=1,
            max_effective_action_force_border_2=2
        )

        self.expected_M = 2.385 #M = 2.385, 7%

    def test_calculations(self):
        calc = Calculator(self.actuator, self.input_data)
        torque = calc.calculate_torque()

        if len(calc.validator.log_list) > 0:
            for log in calc.validator.log_list:
                print(log)

        print("calculated_M = %s\nexpected_M   = %s" % (torque, self.expected_M))
