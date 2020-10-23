# IEOR 4501 Final Project-Squirrel Tracker

## Description
A squirrel tracking app that works with 2018 Central Park Squirrel Census data to visualize the location of squirrels in a map. Besides, users can also update existing record,add new records, and view some statistics regarding the squirrel data. In addtion, this app also allows users to import and export squirrel data.

## Project Group
* Group Name: Struggling Coders
* Section: 1
* Members: Caroline Zhou, Serra Topal Ismail Oglou
* UNIs: [cz2628, st3338 ]

## Application Server
35.231.254.213/sightings/

## Application Features
### Management Commands
1. **Import**

	A command allows users to upload own squirrel data files in CSV extension from custom path. The command should be used at command line:

	```$ python manage.py import_squirrel_data /path/to/file.csv```

2. **Export**

	A command allows users to export squirrels datas from the application to local with custom path and file name in CSV file. The command should be used at command line:

	```$ python manage.py export_squirrel_data /path/to/file.csv```

### Views
1. **Map** 

	Visualize squirrels' spotted location on map. To not crash the application, only 100 of squirrels are viewed at one time. If wish to visualize more, source code will need to be changed.

	Located at: **/map**

2. **Sightings List**

	A list with unique squirrel ID, spotted date and a link to unique squirrel sighting. Addtionally, an add button allows users to add a new squirrel record to the application.

	Located at: **/sightings/**

3. **Unique Squirrel Sightings**

	A webpage shows latitude, longitude, unique squirrel ID, shift, date and age for each squirrel. Users are allowed to change information regarding individual squirrels on corresponding webpage.

	Located at: **/sightings/<unique-squirrel-id>**

4. **Add Sightings**

	A page with form allows users to add new squirrel records. Can be accessed through the button on Sightings List page.

	Located at: **/sightings/add**

5. **Stats**

	Page with some general statistics reagrding the squirrel records.

	Located at: **/sightings/stats**
