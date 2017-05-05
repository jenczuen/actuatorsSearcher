from searchingEngine.models import MotionProfileType


class AccAndSpeedCalculator:

    @classmethod
    def calculate(cls, input_data):
        if input_data.motion_profile.type is MotionProfileType.acc_and_speed:
            return cls.calculate_for_type_1(input_data)

        if input_data.motion_profile.type is MotionProfileType.total_time:
            return cls.calculate_for_type_2(input_data)

        if input_data.motion_profile.type is MotionProfileType.total_and_acc_time:
            return cls.calculate_for_type_3(input_data)

    @staticmethod
    def calculate_for_type_1(input_data):
        return input_data.motion_profile.v_max, input_data.motion_profile.acc

    @staticmethod
    def calculate_for_type_2(input_data):
        t = input_data.motion_profile.t_total / 2
        a_max = input_data.stroke / (t * t)
        V_max = a_max * input_data.motion_profile.t_total / 2
        return a_max, V_max

    @staticmethod
    def calculate_for_type_3(input_data):
        V_max = 2 * input_data.stroke / \
                (input_data.motion_profile.t_total - input_data.motion_profile.t_acc_dcc)
        a_max = V_max / input_data.motion_profile.t_acc_dcc
        return a_max, V_max