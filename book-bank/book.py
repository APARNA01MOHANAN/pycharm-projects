class book:
    def __init__(self,isbn, title,author,publisher,pages,price,copies):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.publisher=publisher
        self.pages=pages
        self.price=price
        self.copies=copies
    def display(self):
        print(self.title)
        print(f'isbn={self.isbn}')
        print(f'author={self.author}')
        print(f'publisher={self.publisher}')
        print(f'pages={self.pages}')
        print(f'price={self.price}')
        print(f'copies={self.copies}')
    def in_stock(self):
        return True if self.copies>0 else False
    def sell(self):
        if self.in_stock():
            self.copies=self.copies-1
            print(self.copies)
        else:
            print("there is no sufficient copies")

book1 = book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,0)

books=[book1,book2,book3,book4]
for Book in books:
    Book.display()
book_jack=[Book.title for Book in books if Book.author=='Jack']
print(book_jack)


book1.display()
book1.sell()

book2.display()
book2.sell()
book3.display()
book3.sell()
book4.display()
book4.sell()