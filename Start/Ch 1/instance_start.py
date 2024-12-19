# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is mlem secret attribute"


    # TODO: create instance methods
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "mlem", 32, 32.33)
b2 = Book("The Catcher in the Rye", "mlem mlem", 2312, 99.99)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.30)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)
