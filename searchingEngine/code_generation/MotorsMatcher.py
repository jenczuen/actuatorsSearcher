import math
from searchingEngine.code_generation.ActuatorsToMotors import ActuatorsToMotors
from searchingEngine.code_generation.GearsToMotors import GearsToMotors
from searchingEngine.code_generation.Motors import Motors


class MotorsMatcher:
    @classmethod
    def choose_mounting_kit(cls, actuator_name, torque, speed, circumference_mm):
        circumference = circumference_mm / 1000
        options = ActuatorsToMotors.map[actuator_name]
        motors_options, gears_options = cls.__split_options(options)
        motor = cls.__find_motor(motors_options, torque, speed, circumference)
        if motor is not None:
            return motor
        motor, gear = cls.__find_motor_with_gear(gears_options, torque, speed, circumference)
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
            motor_code = motor_option[0]
            for key, value in Motors.map.items():
                if key[0] == motor_code:
                    motor_max_torque = value[0]
                    motor_max_rpm = value[1]
                    if cls.__motor_torque_matches(motor_max_torque, torque) and \
                            cls.__motor_speed_matches(motor_max_rpm, speed, circumference):
                        return motor_max_torque
        return None

    @classmethod
    def __motor_torque_matches(cls, motor_max_torque, torque):
        return torque < motor_max_torque

    @classmethod
    def __motor_speed_matches(cls, motor_max_rpm, speed, circumference):
        return cls.__rpm_min_for_m_s(speed, circumference) < motor_max_rpm

    @classmethod
    def __find_motor_with_gear(cls, gears_options, out_torque, out_speed, circumference):
        for gear_option in gears_options:
            cls.__check_max_torque_for_gear(gear_option, out_torque)
            motors_for_gears = GearsToMotors.map[gear_option]
            for ratio in [3, 5, 7, 10, 20]:
                in_torque = out_torque/ratio
                cls.__check_max_torque_for_gear(gear_option, in_torque)
                in_speed = out_speed*ratio
                motor = cls.__find_motor(motors_for_gears, in_torque, in_speed, circumference)
                if motor is not None:
                    return motor, gear_option
        return None

    @classmethod
    def __check_max_torque_for_gear(cls, gear, torque):
        pass

    @classmethod
    def __rpm_min_for_m_s(cls, m_s, circumference):
        return (60 * m_s) / (math.pi * circumference)
