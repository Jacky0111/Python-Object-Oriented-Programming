"""
This code defines two classes, Book and Library. The Library class represents a library, which has a list of
books that can be added, removed, and searched. The Book class represents a book, with a title, author, and year of
publication.

The Library class has methods to add and remove books, and to search for a book by its title. The Book class has a
__repr__ method that returns a string representation of the book.

The code creates a Library object with three books and adds a fourth book using the add_book method. It then searches
for a book by its title using the search_book method, and removes a book that is not in the library (which raises a
ValueError).

The output of the code is the book found by the search (1984 by George Orwell), followed by a ValueError because the
book being removed (The Great Gatsby) is not in the library.
"""


class Library:
    def __init__(self, books):
        self._books = books

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        if book not in self._books:
            raise ValueError("Book not found")
        self._books.remove(book)

    def search_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"{self.title} by {self.author}, published in {self.year}"


library = Library([
    Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949)
])

library.add_book(Book("Pride and Prejudice", "Jane Austen", 1813))
print(library.search_book("1984"))  # Output:

library.remove_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))  #

'''
Output
------
1984 by George Orwell, published in 1949
Raises ValueError: Book not found
'''
