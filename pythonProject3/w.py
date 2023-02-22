class Book:
    books = []

    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
        self.__class__.books.append(self)

    @classmethod
    def bookdetails(cls):
        while True:
            print("1. Enter the book details")
            print("2. Display all the books")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                isbn = input("Enter ISBN: ")
                title = input("Enter title: ")
                author = input("Enter author: ")
                publisher = input("Enter publisher: ")
                pages = int(input("Enter number of pages: "))
                price = float(input("Enter price: "))
                copies = int(input("Enter number of copies: "))
                Book(isbn, title, author, publisher, pages, price, copies)
            elif choice == 2:
                for book in cls.books:
                    print("ISBN:", book.isbn)
                    print("Title:", book.title)
                    print("Author:", book.author)
                    print("Publisher:", book.publisher)
                    print("Pages:", book.pages)
                    print("Price:", book.price)
                    print("Copies:", book.copies)
                    print("-" * 20)
            elif choice == 3:
                break
            else:
                print("Invalid choice, try again")
