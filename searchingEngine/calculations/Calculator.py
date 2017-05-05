from searchingEngine.calculations.CalculatorForSingleModel import CalculatorForSingleModel


class Calculator:

    @staticmethod
    def filter_matching_actuators(actuators, input_data, additional_validation_callback=None):
        results = {}
        for actuator in actuators:
            result = CalculatorForSingleModel(actuator, input_data).calculate_result()
            if additional_validation_callback is not None:
                additional_validation_callback(actuator, result)
            if result.passed_validation():
                results[actuator] = result

        return results

