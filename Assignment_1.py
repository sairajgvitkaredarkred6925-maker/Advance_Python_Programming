class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

class Patron:
    def __init__(self, name):
        self.name = name
        self.books = []

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title):
        self.books.append(Book(title))

    def register_patron(self, name):
        self.patrons.append(Patron(name))

    def borrow_book(self, patron_name, book_title):
        patron = next((p for p in self.patrons if p.name == patron_name), None)
        book = next((b for b in self.books if b.title == book_title and not b.is_borrowed), None)
        if patron and book:
            book.is_borrowed = True
            patron.books.append(book)
            print(f"{patron.name} borrowed {book.title}")
        else:
            print("Borrow failed")

    def return_book(self, patron_name, book_title):
        patron = next((p for p in self.patrons if p.name == patron_name), None)
        if patron:
            book = next((b for b in patron.books if b.title == book_title), None)
            if book:
                book.is_borrowed = False
                patron.books.remove(book)
                print(f"{patron.name} returned {book.title}")
            else:
                print("Return failed")

# Example usage
lib = Library()
lib.add_book("1984")
lib.add_book("The Hobbit")
lib.register_patron("Alice")

lib.borrow_book("Alice", "1984")
lib.return_book("Alice", "1984")
