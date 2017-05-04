from django.core.management.base import BaseCommand
from searchingEngine.management.utlis.ModelsLoader import ModelsLoader


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('path_to_csv', type=str)

    def handle(self, *args, **options):
        path_to_csv = options['path_to_csv']
        self.stdout.write("Loading fixtures from %s" % path_to_csv, ending='')
        ModelsLoader.save_actuators_from_file(path_to_csv, lambda msg: self.stdout.write(msg, ending='\n'))
