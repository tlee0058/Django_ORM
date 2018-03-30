Assignment: Users
Create a new app called 'user_login'. Create a new model called 'User' that has the following fields/attributes

![alt tag](https://user-images.githubusercontent.com/32435667/38141787-d624d014-3407-11e8-9c9c-5f7c5705df32.png)


Please do the following

Create a new model called 'User' with the information above.
Successfully create and run the migration files
Using the shell...
Know how to retrieve all users.
Know how to get the last user.
Create a few records in the users
Know how to get the first user.
Know how to get the users sorted by their first name (order by first_name DESC)
Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
(optional) Ninja:
Find a way to validate the data coming in to the shell.  For example, make sure that "name" fields are a minimum length, "email" is a valid email, or that "email" doesn't already exist in the db.