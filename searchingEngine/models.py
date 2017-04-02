from django.db import models


class Actuator(models.Model):
    name = models.CharField(max_length=20)
    carriage_mass = models.FloatField()
    no_load_torque = models.FloatField()
    pulley_circumference_mm = models.IntegerField()
    max_applied_load_Fy = models.IntegerField()
    max_applied_load_Fz = models.IntegerField()
    max_moment_Mx = models.IntegerField()
    max_moment_My = models.IntegerField()
    max_moment_Mz = models.IntegerField()
    max_stroke_mm = models.IntegerField()
    max_speed = models.IntegerField()
    max_acc = models.IntegerField()
    max_effective_action_force_1 = models.IntegerField()
    max_effective_action_force_2 = models.IntegerField()
    max_effective_action_force_3 = models.IntegerField()
    max_effective_action_force_border_1 = models.IntegerField()
    max_effective_action_force_border_2 = models.IntegerField()

    @staticmethod
    def get_all_actuators_for_display():
        result = []
        for a in Actuator.objects.all():
            result.append({
                'name': a.name
            })
        result.append({'name': 'dummy1'})
        result.append({'name': 'dummy2'})
        return result


class Data:
    pass
