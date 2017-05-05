from searchingEngine.calculations.CalculatorForSingleModel import CalculatorForSingleModel


class Calculator:

    @staticmethod
    def calculate_all(actuators, input_data, additional_validation_callback=None):
        results = {}
        for actuator in actuators:
            result = CalculatorForSingleModel(actuator, input_data).calculate_result()
            if additional_validation_callback is not None:
                additional_validation_callback(actuator, result)
            results[actuator] = result

        return results

