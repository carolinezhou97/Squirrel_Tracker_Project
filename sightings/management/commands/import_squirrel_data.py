import csv
import datetime
import re
from django.core.management.base import BaseCommand, CommandError

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Import squirrel data from custom path'

    def bool(self,arg):
        if arg.lower() == 'True':
            return True
        else:
            return False


    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='/path/to/file.csv')

    
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        
        with open(path) as fp:
            table = csv.reader(fp)

            title = True
            
            ID = []
            rows =[]
            for row in table:
                if row[2] not in ID:
                    ID.append(row[2])
                    rows.append(row)

            for row in rows:
            
                if title:
                    title = False
                
                else:
                
                    if row[4] == 'AM':
                        Shift_temp = Squirrel.AM
                    else:
                        Shift_temp = Squirrel.PM

                    if row[7] == 'Adult':
                        Age_temp = Squirrel.ADULT
                    elif row[7] == 'Juvenile':
                        Age_temp = Squirrel.JUVENILE
                    else:
                        Age_temp = Squirrel.UNKNOWN

                    if row[8] == 'Gray':
                        Fur_Color_temp = Squirrel.GRAY
                    elif row[8] == 'Cinnamon':
                        Fur_Color_temp = Squirrel.CINNAMON
                    elif row[8] == 'Black':
                        Fur_Color_temp = Squirrel.BLACK
                    else:
                        Fur_Color_temp = Squirrel.UNKNOWN

                    if row[12] == 'Ground Plane':
                        Location_temp = Squirrel.GROUND_PLANE
                    if row[12] == 'Above Ground':
                        Location_temp = Squirrel.ABOVE_GROUND
                    else:
                        Location_temp = Squirrel.UNKNOWN


                    squirrel = Squirrel.objects.get_or_create(
                        Longitude = float(row[0]),
                        Latitude = float(row[1]),
                        Unique_Squirrel_ID = row[2],
                        Shift = Shift_temp,
                        Date = datetime.date(int(row[5][-4:]),int(row[5][:2]),int(row[5][2:4])),
                        Age = Age_temp,
                        Fur_Color = Fur_Color_temp,
                        Location = Location_temp,
                        Specific_Location = row[14],
                        Running = self.bool(row[15]),
                        Chasing = self.bool(row[16]),
                        Climbing =self.bool(row[17]),
                        Eating = self.bool(row[18]),
                        Foraging =self.bool(row[19]),
                        Other_Activities = row[20],
                        Kuks = self.bool(row[21]),
                        Quaas = self.bool(row[22]),
                        Moans = self.bool(row[23]),
                        Tail_Flags = self.bool(row[24]),
                        Tail_Twitches = self.bool(row[25]),
                        Approaches = self.bool(row[26]),
                        Indifferent = self.bool(row[27]),
                        Runs_From = self.bool(row[28]),
                    )



