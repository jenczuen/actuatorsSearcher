import csv
import os

from django.core.management.base import BaseCommand, CommandError
from searchingEngine.models import Actuator


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('path_to_csv', type=str)

    def handle(self, *args, **options):
        self.stdout.write("HALKO")

        path_to_csv = options['path_to_csv']
        self.stdout.write(path_to_csv, ending='')

        with open(path_to_csv + 'actuators_fixtures.csv', 'rt') as csvfile:
            self.stdout.write("going to load %s" % csvfile)
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            header = next(reader)
            raw_models = []
            for row in reader:
                raw_model = {}
                for i, item in enumerate(row):
                    raw_model[header[i]] = item
                raw_models.append(raw_model)

            models = []
            for raw_model in raw_models:
                models.append(self.actuator_from_raw_model(raw_model))

            for model in models:
                self.stdout.write(model, ending='')

    def actuator_from_raw_model(self, raw_model):
        return Actuator.objects.get_or_create(
            name=raw_model["name"],
            carriage_mass=raw_model["carriage_mass"],
            no_load_torque=raw_model["no_load_torque"],
            pulley_circumference_mm=raw_model["pulley_circumference_mm"],
            max_applied_load_Fy=raw_model["max_applied_load_Fy"],
            max_applied_load_Fz=raw_model["max_applied_load_Fz"],
            max_moment_Mx=raw_model["max_moment_Mx"],
            max_moment_My=raw_model["max_moment_My"],
            max_moment_Mz=raw_model["max_moment_Mz"],
            max_stroke_mm=raw_model["max_stroke_mm"],
            max_speed=raw_model["max_speed"],
            max_acc=raw_model["max_acc"],
            max_effective_action_force_1=raw_model["max_effective_action_force_1"],
            max_effective_action_force_2=raw_model["max_effective_action_force_2"],
            max_effective_action_force_3=raw_model["max_effective_action_force_3"],
            max_effective_action_force_border_1=raw_model["max_effective_action_force_border_1"],
            max_effective_action_force_border_2=raw_model["max_effective_action_force_border_2"]
        )


