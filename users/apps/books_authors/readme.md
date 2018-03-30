Assignment: Books/Authors

![alt tag](https://user-images.githubusercontent.com/32435667/38143915-a52258de-3410-11e8-897d-186141308887.png)

Create a new app called 'book_authors' in the same project where you did the previous assignment: Dojo Ninjas.  You'll use this assignment as well as the previous assignment to learn about Ajax.

Please do the following

Create a new model called 'Book' with the information above.
Create a new model called 'Author' with the information above.  Design the models in a way that you could perform the following:
Book.objects.first().authors
Author.objects.first().books
Successfully create and run the migration files
Using the shell...
Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
Create 5 different authors: Mike, Speros, John, Jadee, Jay
Add a new field in the authors table called 'notes'.  Make this a TextField.  Successfully create and run the migration files.
Using the shell...
Change the name of the 5th book to C#
Change the first_name of the 5th author to Ketul
Assign the first author to the first 2 books
Assign the second author to the first 3 books
Assign the third author to the first 4 books
Assign the fourth author to the first 5 books (or in other words, all the books)
For the 3rd book, retrieve all the authors
For the 3rd book, remove the first author
For the 2nd book, add the 5th author as one of the authors
Find all the books that the 3rd author is part of
Find all the books that the 2nd author is part of