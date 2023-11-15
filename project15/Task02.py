class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"Library({self.name})"

    def __repr__(self):
        return f"Library({self.name})"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __str__(self):
        return f"Book({self.name}, {self.year}, {self.author.name})"

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author.name})"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"


# Example usage:
library = Library("My Library")

author1 = Author("John Doe", "USA", "1990-01-01")
author2 = Author("Jane Smith", "UK", "1985-03-15")

book1 = library.new_book("Book One", 2020, author1)
book2 = library.new_book("Book Two", 2022, author1)
book3 = library.new_book("Book Three", 2021, author2)

print(book1)
print(library.group_by_author(author1))
print(library.group_by_year(2021))

print(f"Total books created: {Book.total_books}")