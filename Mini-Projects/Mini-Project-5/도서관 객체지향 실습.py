from abc import ABC, abstractmethod

class PrintedMaterial(ABC):
    @abstractmethod
    def info(self):
        pass

class Book(PrintedMaterial):
    
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def info(self):
        return f"{self.title} by {self.author}({self.year})"

    def __lt__(self, other):
        return self.year < other.year
    
class Library:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} loaned successfully!")
        
    def return_book(self, book_title):
        for book in self.books:
            if book_title == book_title:
                self.books.remove(book)
                print(f"{book_title} returned successfully!")
    
    def __del__(self):
        print(f"{self.name} library has been closed.")

    def get_books(self):
        return self.__books

    def set_books(self, books):
        self.__books = books

    books = property(get_books, set_books)

class Novel(Book):
    def __init__(self, title, author, publisher, year, genre):
        super().__init__(title, author, publisher, year)
        self.genre = genre
    def info(self):
        return f"{super().info()} - Genre: {self.genre}"
class Magazine(Book):
    def __init__(self, title, author, publisher, year, month):
        super().__init__(title, author, publisher, year)
        self.month = month
    def info(self):
        return f"{super().info()} - Genre: {self.month}호"
class Text(Book):
    def __init__(self, title, author, publisher, year, subject):
        super().__init__(title, author, publisher, year)
        self.subject = subject
    def info(self):
        return f"{super().info()} - Genre: {self.subject}"
    
def LibraryPass():
    my_lib = Library("서이도서관", "서울시 서초구")
    while 1:
        print("\n1: Book Loans, 2: Return Books, 3: List of Book Loans, 4: Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Book Title: ")
            author = input("Book Author: ")
            publisher = input("Book Publisher: ")
            year = input("Book Year: ")
            book = Book(title, author, publisher, year)
            my_lib.add_book(book)
        elif choice == "2":
            name = input("Book Title to return: ")
            my_lib.return_book(title)
        elif choice == "3":
            for book in my_lib.get_books():
                print(f"{book.title} ({book.author}), 출판사: {book.publisher}")
        elif choice == "4":
            break

LibraryPass()