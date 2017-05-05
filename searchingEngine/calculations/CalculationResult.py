class CalculationResult:
    def __init__(self, torque, sum_of_combined_load, torque_load, errors=None, calculation_steps=None):
        self.torque = torque
        self.sum_of_combined_load = sum_of_combined_load
        self.torque_load = torque_load
        self.errors = errors
        self.calculation_steps = calculation_steps

    def passed_validation(self):
        return self.errors is None or len(self.errors) == 0

    def print_calculation_steps(self):
        for step in self.calculation_steps:
            print(step)

    def print_errors(self):
        for step in self.calculation_steps:
            print(step)
