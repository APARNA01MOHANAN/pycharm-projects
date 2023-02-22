from abc import ABC, abstractmethod
class Book(ABC):
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def in_stock(self):
        pass

    @abstractmethod
    def sell(self):
        pass
class Book_details(Book):
    def get_details(self):
        book_dict = {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "pages": self.pages,
            "price": self.price,
            "copies": self.copies
        }
        return book_dict
    def in_stock(self):
        return True if self.copies > 0 else False
    def sell(self):
        if self.in_stock():
            self.copies =self.copies-1
        else:
            print('The book that you want is out of stock')
book_list = []
while True:
    print("\nMenu:")
    print("1. Add Book")
    print("2. Display Book Details")
    print("3. Book in stock")
    print("4. Sell")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        isbn = input("Enter ISBN: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        publisher = input("Enter publisher: ")
        pages = int(input("Enter number of pages: "))
        price = float(input("Enter price: "))
        copies = int(input("Enter number of copies: "))
        book = Book_details(isbn, title, author, publisher, pages, price, copies)
        book_list.append(book)
    elif choice == 2:
        for book in book_list:
            print(book.get_details())
    elif choice == 3:
        if copies>1:
            print("book is in stock")
        else:
            print("Book is out of stock")
    elif choice == 4:
        if copies>1:
            print("book is in stock")
            copies=copies-1
            print("The remaining copies of this book is ",copies)
        else:
            print("Book is out of stock")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Try again.")