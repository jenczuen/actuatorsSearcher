from searchingEngine.tests.utils.TestScenario import TestScenario
from searchingEngine.models import ActuatorType, ActuatorOrientation, InputData, MotionProfile_TotalTime
from searchingEngine.calculations.CalculationResult import CalculationResult


class TestsScenarios:
    items = {
        "Scenario1": TestScenario(
            input_data=InputData(
                actuator_type=ActuatorType.carriage,
                actuator_orientation=ActuatorOrientation.horizontal_top,
                stroke=3.000,
                mass=5,
                distance_of_mass_x=0.020,
                distance_of_mass_y=0.150,
                distance_of_mass_z=0.050,
                motion_profile=MotionProfile_TotalTime(
                    t_total=1.5
                )
            ),
            results_dictionary={
                "OSPE-B-50": CalculationResult(torque=1.929, sum_of_combined_load=0.68, torque_load=0.26),
                "OSPE-BHD2-25": CalculationResult(torque=2.546, sum_of_combined_load=0.17, torque_load=0.08),
                "OSPE-BHD2-32": CalculationResult(torque=4.312, sum_of_combined_load=0.07, torque_load=0.07),
                "OSPE-BHD2-50": CalculationResult(torque=8.703, sum_of_combined_load=0.04, torque_load=0.06),
                "HMRB-15": CalculationResult(torque=1.766, sum_of_combined_load=0.03, torque_load=0.19),
                "HMRB-18": None,
                "HMRB-24": None
            }
        )
    }
