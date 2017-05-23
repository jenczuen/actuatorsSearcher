from searchingEngine.calculations.Validator import Validator
from searchingEngine.calculations.AccAndSpeedCalculator import AccAndSpeedCalculator
from searchingEngine.calculations.CalculationResult import CalculationResult
from searchingEngine.models import ActuatorOrientation
from math import pi


class CalculatorForSingleModel:
    def __init__(self, actuator, input_data):
        self.validator = Validator(actuator)
        self.actuator = actuator
        self.input_data = input_data
        self.calculation_steps = []
        self.validator.validate_max_stroke(input_data.stroke)
        self.g = 9.807

    def calculate_result(self):
        """
        input_data.actuator_type ????????????
        """

        a_max, V_max = AccAndSpeedCalculator.calculate(self.input_data)
        self.validator.validate_Vmax(V_max)
        self.calculation_steps.append("V_max = %s" % V_max)
        self.validator.validate_a(a_max)
        self.calculation_steps.append("a_max = %s" % a_max)

        F_a, F = self._calculate_forces(a_max)
        self.calculation_steps.append("F = %s" % F)

        return self._calculate_result(F, F_a, V_max);

    def _calculate_forces(self, a):
        self.calculation_steps.append("a = %s" % a)

        m_total = self.input_data.mass + self.actuator.carriage_mass
        self.calculation_steps.append("input_data.mass = %s" % self.input_data.mass)
        self.calculation_steps.append("actuator.carriage_mass = %s" % self.actuator.carriage_mass)
        self.calculation_steps.append("m_total = %s" % m_total)

        F_0 = self.actuator.no_load_torque * 2 * pi / self.actuator.pulley_circumference_mm
        self.calculation_steps.append("actuator.no_load_torque = %s" % self.actuator.no_load_torque)
        self.calculation_steps.append("actuator.pulley_circumference_mm = %s" % self.actuator.pulley_circumference_mm)
        self.calculation_steps.append("F_0 = %s" % F_0)

        F_a = m_total * a
        self.calculation_steps.append("F_a = %s" % F_a)

        if self.input_data.actuator_orientation == ActuatorOrientation.horizontal_top or \
                self.input_data.actuator_orientation == ActuatorOrientation.horizontal_bottom or \
                self.input_data.actuator_orientation == ActuatorOrientation.horizontal_side:
            self.calculation_steps.append("F calculated for horizontal orientation")
            return F_a, F_a + F_0
        else:
            self.calculation_steps.append("F calculated for vertical orientation")
            return F_a, F_a + F_0 + self.g * m_total

    def _calculate_result(self, F, F_a, V_max):
        self.validator.validate_Fa(F_a, V_max)
        M_z = self.input_data.distance_of_mass_z * F_a
        self.validator.validate_Mz(M_z)
        self.calculation_steps.append("M_z = %s" % M_z)

        M_y = 0
        if self.input_data.distance_of_mass_z > 0:
            M_y = self.input_data.distance_of_mass_y * F_a
            self.validator.validate_My(M_y)
        self.calculation_steps.append("M_y = %s" % M_y)

        r = self.actuator.pulley_circumference_mm / (2*pi)
        self.calculation_steps.append("r = %s" % r)

        torque = F * r
        self.calculation_steps.append("torque = %s" % torque)

        sum_of_combined_load = self._calculate_sum_of_combined_load(0, 0, 0, M_y, M_z),
        self.calculation_steps.append("sum_of_combined_load = %s" % sum_of_combined_load)

        return CalculationResult(
            torque=torque,
            speed=V_max,
            sum_of_combined_load=self._calculate_sum_of_combined_load(0, 0, 0, M_y, M_z),
            torque_load=0,
            errors=self.validator.log_list,
            calculation_steps=self.calculation_steps
        )

    def _calculate_sum_of_combined_load(self, Fy, Fz, Mx, My, Mz):
        sum_of_combined_load = Fy / self.actuator.max_applied_load_Fy \
               + Fz / self.actuator.max_applied_load_Fz\
               + Mx / self.actuator.max_moment_Mx\
               + My / self.actuator.max_moment_My\
               + Mz / self.actuator.max_moment_Mz
        self.validator.validate_sum_of_combined_load(sum_of_combined_load)
        return sum_of_combined_load
