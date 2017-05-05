import os

from django.test import TestCase

from searchingEngine.calculations.Calculator import Calculator
from searchingEngine.management.utlis.ModelsLoader import ModelsLoader
from searchingEngine.models import Actuator
from searchingEngine.tests.utils.TestsScenarios import TestsScenarios


class ActuatorTests(TestCase):

    path_to_fixtures = "../fixtures/actuators_fixtures.csv"

    def setUp(self):
        filename = os.path.join(os.path.dirname(__file__), ActuatorTests.path_to_fixtures)
        ModelsLoader.save_actuators_from_file(filename, lambda msg: print(msg))

    def test_scenario(self):
        self.perform_test_for_scenario("Scenario1")

    def perform_test_for_scenario(self, scenario_name):
        scenario = TestsScenarios.items[scenario_name]
        print(scenario.get_desc())

        Calculator.calculate_all(
            actuators=Actuator.objects.all(),
            input_data=scenario.input_data,
            additional_validation_callback=lambda a, r: self.additional_validation(a, r, scenario))


    def additional_validation(self, actuator, result, scenario):
        if result.passed_validation():
            self.assert_valid_actuator(actuator, result, scenario)
        else:
            self.assert_invalid_actuator(actuator, result, scenario)

    def assert_valid_actuator(self, actuator, result, scenario):
        if actuator.name in scenario.results_dictionary:
            expected_result = scenario.results_dictionary[actuator.name]
            print("[OK] Actuator %s MUST pass validation and it does" % actuator.name)
            if expected_result is not None:
                print("\texpected   torque = %s\n\tcalculated torgue = %s"
                      % (expected_result.torque, result.torque))

                print("\texpected   sum_of_combined_load = %s\n\tcalculated sum_of_combined_load = %s"
                      % (expected_result.sum_of_combined_load, result.sum_of_combined_load))

                result.print_calculation_steps()
            print()
        else:
            print("\n[BAD] Actuator %s MUST NOT pass validation but it DOES" % actuator.name)

    def assert_invalid_actuator(self, actuator, result, scenario):
        if actuator.name in scenario.results_dictionary:
            print("\n[BAD] Actuator %s MUST pass validation but it DOES NOT" % actuator.name)
            print(result.torque)
            print(result.sum_of_combined_load)
            result.print_errors()
        else:
            # print("[OK] Actuator %s MUST NOT pass validation and it does not" % actuator.name)
            pass
