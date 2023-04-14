class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def price_per_page(self):
        return self.price / self.pages

    def discount(self, percent):
        self.price *= (1 - percent/100)


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, 12.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281, 9.99)

print(f"{book1.title} by {book1.author}, {book1.pages} pages, ${book1.price:.2f}")
print(f"Price per page: ${book1.price_per_page():.4f}")

print(f"{book2.title} by {book2.author}, {book2.pages} pages, ${book2.price:.2f}")
print(f"Price per page: ${book2.price_per_page():.4f}")

book1.discount(20)
print(f"New price for {book1.title}: ${book1.price:.2f}")


'''
Output
------
The Great Gatsby by F. Scott Fitzgerald, 180 pages, $12.99
Price per page: $0.0722
To Kill a Mockingbird by Harper Lee, 281 pages, $9.99
Price per page: $0.0355
New price for The Great Gatsby: $10.39
'''