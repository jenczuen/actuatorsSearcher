

class Validator:
    def __init__(self, actuator):
        self.actuator = actuator
        self.log_list = []

    def validate_max_stroke(self, value):
        if self.actuator.max_stroke_mm < value:
            self.log_list.append("max_stroke_mm = %s, stroke = %s"
                                 % (self.actuator.max_stroke_mm, value))

    def validate_Mz(self, value):
        if self.actuator.max_moment_Mz < value:
            self.log_list.append("max_moment_Mz = %s, Mz = %s"
                                 % (self.actuator.max_moment_Mz, value))

    def validate_My(self, value):
        if self.actuator.max_moment_My < value:
            self.log_list.append("max_moment_My = %s, My = %s"
                                 % (self.actuator.max_moment_My, value))

    def validate_Fa(self, Fa, Vmax):
        if Vmax <= self.actuator.max_effective_action_force_border_1:
            self._validate_Fa1(Fa)
        elif Vmax <= self.actuator.max_effective_action_force_border_2:
            self._validate_Fa2(Fa)
        else:
            self._validate_Fa3(Fa)

    def _validate_Fa1(self, value):
        if self.actuator.max_effective_action_force_1 < value:
            self.log_list.append("max_effective_action_force_1 = %s, Fa = %s"
                                 % (self.actuator.max_effective_action_force_1, value))

    def _validate_Fa2(self, value):
        if self.actuator.max_effective_action_force_2 < value:
            self.log_list.append("max_effective_action_force_2 = %s, Fa = %s"
                                 % (self.actuator.max_effective_action_force_2, value))

    def _validate_Fa3(self, value):
        if self.actuator.max_effective_action_force_3 < value:
            self.log_list.append("max_effective_action_force_3 = %s, Fa = %s"
                                 % (self.actuator.max_effective_action_force_3, value))

    def validate_Vmax(self, value):
        if self.actuator.max_speed < value:
            self.log_list.append("max_speed = %s, Vmax = %s"
                                 % (self.actuator.max_speed, value))

    def validate_a(self, value):
        if self.actuator.max_acc < value:
            self.log_list.append("max_acc = %s, a = %s"
                                 % (self.actuator.max_acc, value))