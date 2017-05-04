import csv
from searchingEngine.models import Actuator


class ModelsLoader:

    @staticmethod
    def save_actuators_from_file(path_to_csv, print_function, object_type="ACTUATOR"):
        print_function("Loading fixtures from %s" % path_to_csv)

        with open(path_to_csv, 'rt') as csvfile:
            print_function("Opened %s" % csvfile)
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            header = next(reader)
            raw_models = []
            for row in reader:
                raw_model = {}
                for i, item in enumerate(row):
                    raw_model[header[i]] = item
                raw_models.append(raw_model)

            for raw_model in raw_models:
                if object_type == "ACTUATOR":
                    model_tuple = ModelsLoader.__get_or_create_actuator_for_raw_model(raw_model)
                    model = model_tuple[0]
                    status = model_tuple[1]
                    print_function("Name = %s, %s" % (model.name,
                                                      "not present in db, saving..." if status is True else "already present in db"))

    @staticmethod
    def __get_or_create_actuator_for_raw_model(raw_model):
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

