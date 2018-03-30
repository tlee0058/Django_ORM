Assignment: Dojo Ninjas
Create a new app called 'dojo_ninjas'. For this project, you're going to need the following tables/models. Please see the following diagram and create the necessary model:

![alt tag](https://user-images.githubusercontent.com/32435667/38142694-58d506b6-340b-11e8-99c5-062430690314.png)

Dojo
Have it include the name of the dojo and the city and state of each dojo
Have the first dojo be "CodingDojo Silicon Valley" in "Mountain View", "CA".
Have the second dojo be "CodingDojo Seattle" in "Seattle", "WA".
Have the third dojo be "CodingDojo New York" in "New York", "NY".
Ninja
Have it include first_name, last_name of each ninja in the dojo.
Each dojo can have multiple ninjas and each ninja belongs to a specific dojo.
This is what you'll do:

Start a new app (the name of the app should be 'dojo_ninjas')
Create appropriate tables/models that allows you to perform tasks such as
Dojo.objects.first().ninjas.all()
Ninja.objects.first().dojo
Using Django Shell:
Create 3 dojos
Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())
Create 3 additional dojos by using Dojo.objects.create
Create 3 ninjas that belong to the first dojo you created.
Create 3 more ninjas and have them belong to the second dojo you created.
Create 3 more ninjas and have them belong to the third dojo you created.
Be able to retrieve all ninjas that belong to the first Dojo
Be able to retrieve all ninjas that belong to the last Dojo
Add a new field in the Dojo class (found in your models.py) called 'desc'. Allow 'desc' to hold long text (more than 255 characters). To forward engineer the change, run the appropriate migration commands. Successfully run the migration files and check the records to make sure the new field was added successfully.