from searchingEngine.calculations.CalculatorForSingleModel import CalculatorForSingleModel


class Calculator:

    @staticmethod
    def filter_matching_actuators(actuators, input_data, additional_validation_callback=None):
        results = {}
        for actuator in actuators:
            calculation_result = CalculatorForSingleModel(actuator, input_data).calculate_result()
            if additional_validation_callback is not None:
                additional_validation_callback(actuator, calculation_result)

            if calculation_result.passed_validation():
                results[actuator] = calculation_result

        return results

