class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} by {self.author} is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} by {self.author} was not checked out.")

    def is_checked_out(self):
        return self._is_checked_out
    
class Library:
    def __init__(self):
        self._books = []  

    def add_book(self, book):
        self._books.append(book)
        print(f"Added {book.title} by {book.author} to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out():
                    book.check_out()
                    return
                else:
                    print(f"The book '{title}' is already checked out.")
                    return
        print(f"The book '{title}' is not available in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_checked_out():
                    book.return_book()
                    return
                else:
                    print(f"The book '{title}' was not checked out.")
                    return
        print(f"The book '{title}' is not available in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are available for checkout at the moment.")
