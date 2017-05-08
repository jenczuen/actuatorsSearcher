import math
from searchingEngine.code_generation.ActuatorsToMotors import ActuatorsToMotors
from searchingEngine.code_generation.GearsToMotors import GearsToMotors


class MotorsMatcher:
    @classmethod
    def choose_mounting_kit(cls, actuator_name, torque, speed, circumference_mm):
        options = ActuatorsToMotors.map[actuator_name]
        motors_options, gears_options = cls.__split_options(options)
        motor = cls.__find_motor(motors_options, torque, speed, circumference_mm / 1000)
        if motor is not None:
            return motor
        motor, gear = cls__.find_motor_with_gear(gears_options)
        if motor is not None and gear is not None:
            return motor + ", " + gear
        return "pucha2"

    @classmethod
    def __split_options(cls, options):
        motors_options = []
        gears_options = []
        for option in options:
            if isinstance(option, str):
                gears_options.append(option)
            elif isinstance(option, tuple):
                motors_options.append(option)
        return motors_options, gears_options

    @classmethod
    def __find_motor(cls, motors_options, torque, speed, circumference):
        for motor_option in motors_options:
            if cls.__motor_torque_matches(motor_option[0], torque) and \
                    cls.__motor_speed_matches(motor_option[1], speed, circumference):
                return motor_option[0]
        return None

    @classmethod
    def __motor_torque_matches(cls, motor_max_torque, torque):
        return torque < motor_max_torque

    @classmethod
    def __motor_speed_matches(cls, motor_max_rpm, speed, circumference):
        speed_rpm = (60 * speed) / (math.pi * circumference)
        return speed_rpm < motor_max_rpm

    @classmethod
    def find_motor_with_gear(cls, gears_options, torque, speed, circumference):
        for gear_option in gears_options:
            # sprawdzanie czy torque nie jest za duzy dla geara
            motors_for_gears = GearsToMotors.map[gear_option]
            for ratio in []:
                gear_torque = torque*ratio
                # sprawdzanie czy gear_torque nie jest za duzy dla geara
                gear_speed = speed/ratio
                motor = cls.__find_motor(motors_for_gears, gear_torque, gear_speed, circumference)
                if motor is not None:
                    return motor, gear_option
        return None
