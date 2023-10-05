# Create a class called "Library" that represents a 
#library system. Include attributes such as a list of books, available seats,
#and a librarian. Implement methods to add books to the library, check out books,
#and display the current status of available seats.
class Library:
    def __init__(self,books,seats,librarian):
        self.books=books
        self.seats=seats
        self.librarian=librarian
    def add_books(self,new_books):
        self.books=new_books
        new_books=[]
        new_books+=1
        return new_books
    def check_out(self):
        books=[]
        books-=1
        return books
    def display_seat(self):
        print("Available seats",self.seats)
        print("Available Books", self.books)
        print("The libararian is ", self.librarian)

lib=Library("River and The Source",5,"Samson")
lib.add_books("ABC")
lib.display_seat()