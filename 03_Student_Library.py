class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Books present in this libarary are: ")
        for book in self.books:

            print("\t *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.Please Keep it safe and return it with in 30days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry , This book has already issued to someone else.  Please wait until the book is returned")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print('''Thanks for returning this book! Hope you enjoyed reading it . 
        OR
        Thanks for Donating
        Have a great day ahead!''')


class Student:
    def requestBook(self):
        self.book = input("Enter the name of thre book you want to barrow .")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of thre book you want to return .")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "clrs", "Balgurusammay OOP's", "Ross & kolman Discrete Mathemathics","Harrdy Boyz", "Gossebumps"])
    Student = Student()
    centralLibrary.displayAvailableBooks()

    while(True):
        welcomeMsg = '''!!!!Welcome to central library !!!!
        Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''

        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a ==2:
            centralLibrary.borrowBook(Student.requestBook())
        elif a ==3:
            centralLibrary.returnBook(Student.returnBook())
        elif a ==4:
            print("Thanks for using Central Library.Have a great Day.")
            exit()
            

        
        