class Book:
    def __init__(self,title,author,availability = True):

        #Assign to self object
        self.title = title
        self.author = author
        self.availability = True

    def get_details(self):
            return f'Title:{self.title},Author:{self.author},Availability:{self.availability}'
        
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def view_book(self):
        for book in self.books:
            print (book.get_details())

    def borrow_book(self,title):
         for book in self.books:
              if book.title == title:
                   if book.availability:
                        book.availability = False
                        print(f'{book.title} has been borrowed')
                   else:
                        print(f'{book.title} is already borrowed')
                        return
    print('Book not found')
        

    def return_book(self,title):
         for book in self.books:
              if book.title == title:
                   if not book.availability:
                        book.availability = True
                        print(f'You returned {book.title}')
                   else:
                        print(f'{book.title} was not borrowed')
                        return
                   print('Book not found')
        


#Main program
library = Library() #Object creation for the class library


book_1 = Book('RDPD','Robert Kiyosaki') #Object creation for the class book
book_2 = Book('Red Heifer','Peggy Oppong')
book_3 = Book('RDPC','Robert Kiyosaki')
book_4 = Book('RDPE','Robert Kiyosaki')
book_5 = Book('RDPF','Robert Kiyosaki')

Books = [book_1, book_2, book_3, book_4, book_5]
for book in Books:
     library.add_book(book)

# Test cases
library.borrow_book('RDPD')
library.return_book('RDPD')
library.view_book()


