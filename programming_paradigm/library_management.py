class Book:
    """A class for a list of books in a library"""
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def check_out(self,book):
        self._is_checked_out = True  
        
    def return_book(self,book):
        self._is_checked_out = False  
        
    def is_available(self, book):
        return not self._is_checked_out
        
    
    
    
    
class Library:
    def __init__(self):
        self._books = []
        pass
    
    def add_book(self, book):
        self._books.append(book)
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available(book):
                book.check_out(book)
                return True    
        return False
       
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available(book):
                book.retun_book(book)
                return True
            return False
        
   
    def list_available_books(self):
        for book in self._books:
            if book.is_available(book):
                print(f"{book.title} by {book.author}")
    
    
    