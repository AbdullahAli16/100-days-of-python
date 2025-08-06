# Day: 63(Ex: 5 Snake, Water and Gun solution)

# Day: 64(Ex: 6 Library Management System)

'''Books would be a list, no_of_book is an integer, when you add books the no_of_books should increase
    make a method which will check if no of books= len(books) and if its not true print somethings is wrong
    with your program. Make 3 libraries from library class. make method of printing all books, add a book,
    subtract a book, get the numberofbooks. show that your praogram does'nt persist the books after
    the program is stopped'''
    
class Library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0
        
    
    def add_book(self,*args):            # Add a book
        self.books.extend(args)
        self.no_of_books+=len(args)
        print("Book added successfully.")
        print(f"Now books list is: {self.books}")
    
    def remove_book(self,*args):          # Remove a book
        for item in args:
            if item in self.books:
                self.books.remove(item)       
                self.no_of_books-=1
                print("Book removed successfully.")
                print(f"Now books list is: {self.books}")
            else:
                print("Error, book not found in the books list")
        
    def check_length(self):                 # Double check length
        if self.no_of_books==len(self.books):
            print("Your program is working correctly")
        else:
            print(f"Oops, there is something wrong with your program")
            print(f"because no of books is {self.no_of_books}, and books is {self.books}")
        
    def all_books(self):                     # Prints all books
        print("This is the list of all books")
        for index, book in enumerate(self.books):
            print(f"Book no: {index+1} is {book}")
            
            
library_1= Library()
library_2= Library()
library_3= Library()

print(f"As you can see the books list is empty for now:{library_1.books}")
library_1.add_book("book3","book4","book5")


library_1.remove_book("book3","book4")
library_1.all_books()
library_1.check_length()