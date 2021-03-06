# Generated by Django 3.1.2 on 2020-10-16 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(help_text='Latitude of squirrel location')),
                ('Longitude', models.FloatField(help_text='Longitude of squirrel location')),
                ('Unique_Squirrel_ID', models.CharField(help_text='Unique ID for each squirrel', max_length=100, unique=True)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Whether sighting session occurred in the morning or late afternoon', max_length=2)),
                ('Date', models.DateField(help_text='Sighting date')),
                ('Age', models.CharField(choices=[('Adult', 'Adult'), (' Juvenile', 'Juvenile'), ('unknown', 'Unkown')], default='unknown', help_text='Age of squirrel', max_length=100)),
                ('Fur_Color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('Unknown', 'Unknown')], default='Unknown', help_text='Primary fur color', max_length=100)),
                ('Location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), ('Unknown', 'Unknown')], default='Unknown', help_text='Where the squirrel was when first sighted', max_length=100)),
                ('Specific_Location', models.CharField(help_text='Commentary on the squirrel location', max_length=100)),
                ('Running', models.BooleanField(default=False, help_text='Squirrel was seen running')),
                ('Chasing', models.BooleanField(default=False, help_text='Squirrel was seem chasing another squirrel')),
                ('Climbing', models.BooleanField(default=False, help_text='Squirrel was seen climbing a tree or other environmental landmark')),
                ('Eating', models.BooleanField(default=False, help_text='Squirrel was seen eating')),
                ('Foraging', models.BooleanField(default=False, help_text='Squirrel was seen foraging for food')),
                ('Other_Activities', models.CharField(help_text='Other noticed activitied', max_length=100)),
                ('Kuks', models.BooleanField(default=False, help_text='Squirrel was heard kukking')),
                ('Quaas', models.BooleanField(default=False, help_text='Squirrel was heard quaaing')),
                ('Moans', models.BooleanField(default=False, help_text='Squirrel was heard moaning')),
                ('Tail_Flags', models.BooleanField(default=False, help_text='Squirrel was seen flagging its tail')),
                ('Tail_Twitches', models.BooleanField(default=False, help_text='Squirrel was seen switching its tail')),
                ('Approaches', models.BooleanField(default=False, help_text='Squirrel was seen approachhing human, seeking food')),
                ('Indifferent', models.BooleanField(default=False, help_text='Squirrel was indifferent to human presence')),
                ('Runs_From', models.BooleanField(default=False, help_text='Squirrel was seen running from humans, seeing them as a threat')),
            ],
        ),
    ]
