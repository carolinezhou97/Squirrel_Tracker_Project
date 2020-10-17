from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel

import pandas as pd

class Command(BaseCommand):

    help='export squirrel dat to csv file to custom path'

    def add_arguments(self,parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.DataFrame(Squirrel.objects.all().values())
        df.to_csv(path)

