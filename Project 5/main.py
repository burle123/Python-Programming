'''
Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!
'''

class Library:
    def __init__(self): 
        self.books = [] 
        self.no_of_books = 0 

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        print(f'Book "{book_name}" added to the library.')

    def get_number_of_books(self):
        print(f"No. of Books added into Library = {self.no_of_books}") 
    def print_all_books(self):
        if self.no_of_books == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f'- {book}')


L1 = Library()
L1.add_book("Rich Dad Poor Dad")
L1.add_book("Atomic Habits")
L1.add_book("Think and Grow Rich")
L1.get_number_of_books()
L1.print_all_books()

