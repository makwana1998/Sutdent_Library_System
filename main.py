class Library:

    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present in this Library are: ")
        for book in self.books:
            print(" >>> " + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You Have been issued {bookName}. Please keep it safe and Return it within 30 Days")
            self.books.remove(bookName)
            return True
        else:
            print("Soory, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
        
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    
    def returntBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
    

if __name__ == "__main__":
    centralLibrary = Library(["Python","Machin Learing","JavaScript","C language"])
    # centralLibrary.displayAvailableBooks()
    student = Student()

    while(True):
        WelcomeMsg = '''===== Welcome to Central Library =====

        Please choose an option:

        1. List Of All Book
        2. Request a book
        3. Add OR Return a book
        4. Exit the Library
        '''
        print(WelcomeMsg)
        
        p = int(input("Enter a Choice: "))

        if p == 1:
            centralLibrary.displayAvailableBooks()
        elif p ==2:
            centralLibrary.borrowBook(student.requestBook())
        elif p ==3:
            centralLibrary.returnBook(student.returntBook())
        elif p ==4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Your Choice!")
            