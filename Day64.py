# # Exercise - 6... Question... Library Management System... 




# Write a library class with no_of_books and books as two instance variable. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesn't persist the books after the program is stopped...









class Library:

    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showBooks(self):
        print("Books Available in Library:")

        for book in self.books:
            print(book)

    def getNumberOfBooks(self):
        print("Total Number of Books:", self.no_of_books)


# Creating Library Object

library = Library()

# Adding Books

library.addBook("Python")
library.addBook("Java")
library.addBook("C++")
library.addBook("Data Science")
library.addBook("TAFL")
library.addBook("Computer Network")
library.addBook("Operating System")
library.addBook("DAA")


# Displaying Books

library.showBooks()

# Displaying Total Number of Books

library.getNumberOfBooks()