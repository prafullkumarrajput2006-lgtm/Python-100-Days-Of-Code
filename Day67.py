# Exercise - 6... Solution... Library Management System... 








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