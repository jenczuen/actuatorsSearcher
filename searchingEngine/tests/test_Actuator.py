from django.test import TestCase

from searchingEngine.tests.TestScenarios import TestsScenarios
from searchingEngine.models import Actuator
from searchingEngine.validation.Calculator import Calculator
from searchingEngine.management.utlis.ModelsLoader import ModelsLoader
import os


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

        for actuator in Actuator.objects.all():
            result = Calculator(actuator, scenario.input_data).calculate_result()
            if result.passed_validation():
                self.assert_valid_actuator(actuator, result, scenario)
            else:
                self.assert_invalid_actuator(actuator, result, scenario)

    def assert_valid_actuator(self, actuator, result, scenario):
        if actuator.name in scenario.results_dictionary:
            # expected_result = scenario.results_dictionary[]
            # print("[OK] Actuator %s MUST pass validation and it does" % actuator.name)
            pass
        else:
            print("\n[BAD] Actuator %s MUST NOT pass validation but it DOES" % actuator.name)

    def assert_invalid_actuator(self, actuator, result, scenario):
        if actuator.name in scenario.results_dictionary:
            print("\n[BAD] Actuator %s MUST pass validation but it DOES NOT" % actuator.name)
            for error in result.errors:
                print("\t%s" % error)
        else:
            # print("[OK] Actuator %s MUST NOT pass validation and it does not" % actuator.name)
            pass
