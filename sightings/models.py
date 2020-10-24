from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Squirrel(models.Model):
    
    Latitude = models.FloatField(
            blank=False,
            help_text=_('Latitude of squirrel location'),
    )

    Longitude = models.FloatField(
            blank=False,
            help_text=_('Longitude of squirrel location'),
    )

    
    Unique_Squirrel_ID = models.CharField(
            max_length=100,
            help_text=_('Unique ID for each squirrel'),
            unique=True,
            blank=False,
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
            (AM, _('AM')),
            (PM, _('PM')),
    ]

    Shift = models.CharField(
            max_length=2,
            help_text=_('Whether sighting session occurred in the morning or late afternoon'),
            choices=SHIFT_CHOICES,
            default=AM,
    )

    Date = models.DateField(
            help_text=_('Sighting date'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'unknown'

    AGE_CHOICES = [
            (ADULT, _('Adult')),
            (JUVENILE, _('Juvenile')),
            (UNKNOWN, _('Unkown')),
    ]

    Age = models.CharField(
            max_length=100,
            help_text=_('Age of squirrel'),
            choices=AGE_CHOICES,
            default=UNKNOWN,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    UNKNOWN = 'Unknown'

    FUR_COLOR_CHOICES= [
            (GRAY, _('Gray')),
            (CINNAMON, _('Cinnamon')),
            (BLACK, _('Black')),
            (UNKNOWN, _('Unknown')),
    ]

    Fur_Color = models.CharField(
            max_length=100,
            help_text=_('Primary fur color'),
            choices=FUR_COLOR_CHOICES,
            default=UNKNOWN,
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    UNKNOWN = 'Unknown'

    LOCATION_CHOICES = [
            (GROUND_PLANE, _('Ground Plane')),
            (ABOVE_GROUND, _('Above Ground')),
            (UNKNOWN, _('Unknown')),
    ]

    Location = models.CharField(
            max_length=100,
            help_text=_('Where the squirrel was when first sighted'),
            choices=LOCATION_CHOICES,
            default=UNKNOWN,
    )

    Specific_Location = models.CharField(
            max_length=100,
            help_text=_('Commentary on the squirrel location'),
    )

    Running = models.BooleanField(
            help_text=_('Squirrel was seen running'),
            default=False,
    )

    Chasing = models.BooleanField(
            help_text=_('Squirrel was seem chasing another squirrel'),
            default=False,
    )

    Climbing = models.BooleanField(
            help_text=_('Squirrel was seen climbing a tree or other environmental landmark'),
            default=False,
    )

    Eating = models.BooleanField(
            help_text=_('Squirrel was seen eating'),
            default=False,
    )

    Foraging = models.BooleanField(
            help_text=_('Squirrel was seen foraging for food'),
            default=False,
    )

    Other_Activities = models.CharField(
            max_length=100,
            help_text=_('Other noticed activitied'),
    )

    Kuks = models.BooleanField(
            help_text=_('Squirrel was heard kukking'),
            default=False,
    )

    Quaas = models.BooleanField(
            help_text=_('Squirrel was heard quaaing'),
            default=False,
    )

    Moans = models.BooleanField(
            help_text=_('Squirrel was heard moaning'),
            default=False,
    )

    Tail_Flags = models.BooleanField(
            help_text=_('Squirrel was seen flagging its tail'),
            default=False,
    )

    Tail_Twitches = models.BooleanField(
            help_text=_('Squirrel was seen switching its tail'),
            default=False,
    )

    Approaches = models.BooleanField(
            help_text=_('Squirrel was seen approachhing human, seeking food'),
            default=False,
    )

    Indifferent = models.BooleanField(      
            help_text=_('Squirrel was indifferent to human presence'),
            default=False,
    )

    Runs_From = models.BooleanField(      
            help_text=_('Squirrel was seen running from humans, seeing them as a threat'),
            default=False,
    )       

    def __str__(self):
        return self.Unique_Squirrel_ID
