Assignment: Login and Registration
Rebuild the Login and Registration assignment from the flask chapter, this time using Django.

We’ve learned how to integrate models, validations, and controllers to our projects. Our next goal is to create a fully functional login and registration app! This will combine your knowledge of MVC patterns, validations, and password encryption.

![alt tag](https://user-images.githubusercontent.com/32435667/38163929-1ff10038-34ca-11e8-85f1-cec113935724.png)

Build the following:
Show validation error messages if validations fail the following tests
First Name - Required; No fewer than 2 characters; letters only
Last Name - Required; No fewer than 2 characters; letters only
Email - Required; Valid Format
Password - Required; No fewer than 8 characters in length; matches Password Confirmation
Bonus: Birthday Field - Before today, or go creative and do it in an age range
Bonus: Implement Flash Messages
login_reg

One thing we've noticed as people build their login and registrations that you should consider:

User.objects.get(email = email)
If there is not a matching email for a .get(), Django throws an error (try and except could come in handy), otherwise it returns the User object associated with the matching user. e.g. Userobject.

User.objects.filter(email = email)
Filter, on the other hand, returns a list, so if there is no user that matches, it returns an empty list.  If there is a single matching user the list will contain a single User object: e.g. [Userobject].