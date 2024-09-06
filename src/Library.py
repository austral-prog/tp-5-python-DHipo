from src.Book import Book
from src.User import User


class Library:
    def __init__(self) -> None:
        self.__books: list[Book] = []
        self.__users: list[User] = []
        self.__checked_out_books: list[list] = []
        self.__checked_in_books: list[list] = []

    # Getters
    def get_books(self) -> list:
        return self.__books

    def get_users(self) -> list:
        return self.__users

    def get_checked_out_books(self) -> list:
        return self.__checked_out_books

    def get_checked_in_books(self) -> list:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        self.__books += [
            Book(isbn, title, author)
        ]

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(str(book))

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: int, due_date: str) -> str:
        if not isbn in [book.get_isbn() for book in self.__books]: 
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

        user_index: int = [user.get_dni() for user in self.__users].index(dni)
        book_index: int = [book.get_isbn() for book in self.__books].index(isbn)

        if not self.__books[book_index].is_available(): return f"Book {isbn} is not available"

        self.__users[user_index].increment_checkouts()

        self.__books[book_index].set_available(False)
        self.__books[book_index].increment_checkout_num()
        self.__checked_out_books += [
            [isbn, dni, due_date]
        ]

        return f"User {dni} checked out book {isbn}"

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: int, returned_date: str) -> str:
        if not isbn in [book.get_isbn() for book in self.__books]: 
            return f"Book {isbn} is not available"
        
        user_index: int = [user.get_dni() for user in self.__users].index(dni)
        book_index: int = [book.get_isbn() for book in self.__books].index(isbn)
        
        if self.__books[book_index].is_available(): return f"Book {isbn} is not available"

        self.__users[user_index].increment_checkins()
        self.__books[book_index].set_available(True)
        
        index = [book_out[1] for book_out in self.__checked_out_books].index(dni)
        del self.__checked_out_books[index]
        
        self.__checked_in_books += [
            [isbn, dni, returned_date]
        ]
        return f"Book {isbn} checked in by user {dni}"


    # Utils
    def add_user(self, dni: int, name: str) -> None:
        self.__users += [
            User(dni, name)
        ]