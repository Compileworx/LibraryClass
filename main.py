class Book(object):
    
    def __init__(self, title, author):
        self._title = str(title)
        self._author = str(author)
        self._queue = []
        self._checkedOut = False
    
    def getTitle(self):
        return str(self._title)
    
    def getAuthor(self):
        return str(self._author)
    
    def isCheckedOut(self):
        return self._checkedOut
    
    def setCurrentPatron(self, patron):
        self._currentPatron = patron
        
    def getCurrentPatron(self):
        return self._currentPatron
    
    def queuePatron(self, patron):
        self._queue.append(patron)
        
    def getQueueCount(self):
        return int(len(self._queue))
    
    def getNextPatron(self):
        return self._queue.pop(0)
    
    def checkOut(self):
        self._checkedOut = True
        
    def checkIn(self):
        self._checkedOut = False
        
class Patron(object):
    
    def __init__(self, patronName):
        self._patronName = str(patronName)
        self._bookCount = 0
    
    def limitReached(self):
        if self._bookCount >= 3:
            return True
        else:
            return False
        
    def addBook(self):
        self._bookCount+=1
        
    def removeBook(self):
        self._bookCount-=1
        
    def getPatronName(self):
        return str(self._patronName)

class Library(object):
    def __init__(self):
        self._patronList = []
        self._bookList = []
    
    def addPatron(self, patronName):
        if len(str(patronName)) > 0:
            p = Patron(patronName)
            self._patronList.append(p)
            return True
        else:
            return False
    
    def addBook(self, bookTitle, bookAuthor):
        if len(str(bookTitle)) > 0 and len(str(bookAuthor)) > 0:
            self._bookList.append(Book(bookTitle, bookAuthor))
            return True
        else:
            return False
    
    def findPatron(self, patronName):
        if len(self._patronList) > 0:
            index = 0
            for o in self._patronList:
                if o != None:
                    if str(o.getPatronName()) == str(patronName):
                        return index
                index += 1
        else:
            return -1
    
    def findBookbyTitle(self, bookTitle):
        if len(self._bookList) > 0:
            index = 0
            for o in self._bookList:
                if o != None:
                    if str(o.getTitle()) == str(bookTitle):
                        return index
                index += 1
        else:
            return -1
        
    def findBookbyAuthor(self, bookAuthor):
        if len(self._bookList) > 0:
            for o in self._bookList:
                if o != None:
                    if str(o.getAuthor()) == str(bookAuthor):
                        return o
        else:
            return None
    
    def deleteBook(self, bookTitle):
        if len(self._bookList) > 0:
            i = 1
            removeAt = 0
            for o in self._bookList:
                if o != None:
                    if str(o.getTitle()) == str(bookTitle):
                        removeAt = i
                i = i + 1
            
            if removeAt > 0:
                self._bookList.pop(removeAt - 1)
                return True
            else:
                return False
            
        else:
            return False
        
    def deletePatron(self, patronName):
        if len(self._patronList) > 0:
            i = 1
            removeAt = 0
            for o in self._patronList:
                if o != None:
                    if str(o.getPatronName()) == str(patronName):
                        removeAt = i
                i = i + 1
            
            if removeAt > 0:
                self._patronList.pop(removeAt - 1)
                return True
            else:
                return False
            
        else:
            return False
        
    def deletePatronByIndex(self, index):
        if len(self._patronList) > 0:
            self._patronList.pop(int(index))
            return True
        else:
            return False
            
        
    def deleteBookByIndex(self, index):
        if len(self._bookList) > 0:
            self._bookList.pop(int(index))
            return True
        else:
            return False
        
    def getPatronList(self):
        return self._patronList
    
    def getBookList(self):
        return self._bookList
    
class Manager(object):
    
    def __init__(self):
        self._library = Library()
        self._exit = False
        self._selection = "0"
    
    def showMenu(self):
        while self._exit == False:
            
            print("Library Menu")
            print("............")
            print("1. Add a Patron")
            print("2. View library Patrons")
            print("3. Search for patron")
            print("4. Add Book")
            print("5. View library Books")
            print("6. Search for book")
            print("7. Get book")
            print("8. Return book")
            print("9. Delete patron")
            print("10.Delete book")
            print("11.Create test data")
            print("0. Exit")
            
            self._selection = input("Please make a selection\n\n")
            
            if self._selection == "1":
                self.addPatron()
            elif self._selection == "2":
                self.viewPatrons()
            elif self._selection == "3":
                self.patronsearch()
            elif self._selection == "4":
                self.addBook()
            elif self._selection == "5":
                self.viewBooks()
            elif self._selection == "6":
                self.bookSearch()
            elif self._selection == "7":
                self.getBook()
            elif self._selection == "8":
                self.returnBook()
            elif self._selection == "9":
                self.deletePatron()
            elif self._selection == "10":
                self.deleteBook()
            elif self._selection == "11":
                self.createTestData()
            elif self._selection == "0":
                self._exit = True
    
    def addPatron(self):
        print("Patron Add")
        print("..........\n")
        patronName = input("Please enter patron name : ")
        self._library.addPatron(patronName)
        
    def addBook(self):
        print("Book Add")
        print("..........")
        bookTitle = input("Please enter the book title : ")
        bookAuthor = input("Please enter the author of the book : ")
        self._library.addBook(bookTitle, bookAuthor)
        
    def viewPatrons(self):
        print("Patron List")
        print("...........\n")
        index = 0
        for o in self._library.getPatronList():
            if o != None:
                print("Index",index , ":",o.getPatronName(),"-> Limit reached :",o.limitReached())
            index += 1
        input("\nPress any key to continue.\n")
        
    def viewBooks(self):
        print("Book List")
        print(".........")
        index = 0
        for o in self._library.getBookList():
            if o != None:
                print("Index",index , "Book Title :",o.getTitle(),"Book Author :",o.getAuthor())
            index += 1
        input("\nPress any key to continue.\n")
        
    def bookSearch(self):
        print("Book Search")
        print("...........")
        bookTitleAuthor = str(input("Please enter a book title or author to search for ? "))
        
        index = self._library.findBookbyTitle(bookTitleAuthor)
        
        if index != -1:
            b = self._library.getBookList()[index]
            print("Book title found at index :",index,"is checked out :",b.isCheckedOut())
        else:
            index = self._library.findBookbyAuthor(bookTitleAuthor)
            
            if index != -1:
                b = self._library.getBookList()[index]
                print("Book author found at index :",index,"is checked out :",b.isCheckedOut())
            else:
                print("Unable to find book by title nor author")
        
        input("Please enter any key to continue.\n")
    
    def patronsearch(self):
        print("Patron Search")
        print(".............")
        patronName = str(input("Please enter a patron name to search for ? "))
        
        index = self._library.findPatron(patronName)
        
        if index != -1:
            p = self._library.getPatronList()[index]
            print("Patron found at index : ",index,"book limit reached",p.limitReached())
        else:
            print("Unknown library patron")
        
        input("Please enter any key to continue.\n")
        
    def getBook(self):
        print("Check Book Out")
        print("..............")
        patronID = int(input("Please enter patron id : "))
        bookID = int(input("Please enter book id : "))
        p = self._patrons[patronID]
        b = self._books[bookID]
        if p.limitReached() == True:
            print("Patron has reached their book limit.")
        else:
            if b.isCheckedOut() == True:
                b.queuePatron(p)
                print("Book is currently out. You have been placed in the queue.")
            else:
                b.checkOut()
                b.setCurrentPatron(p)
                p.addBook()
                print(b.getTitle() + " has has been allocated to " + p.getPatron())
                
        input("Please enter any key to continue.\n")
                
    def returnBook(self):
        print("Return Book")
        print("...........")
        bookID = int(input("Enter the book id returned : "))
        b = self._books[bookID]
        patronID = int(input("Enter the patron id : "))
        p = self._patrons[patronID]
        if b.getQueueCount() > 0:
            pq = b.getNextPatron()
            b.setCurrentPatron(pq)
            pq.addBook()
            print("Book has now been allocated to :" + pq.getPatron())
        else:
            b.checkIn
            b.setCurrentPatron(None) 
        p.removeBook()
        
        input("Please enter any key to continue.\n")
        
    def deletePatron(self):
        print("Delete Patron")
        print(".............")
        
        patronName = str(input("Please enter the patron you wish to delete : "))
        patronDeleted = self._library.deletePatron(patronName)
        
        if patronDeleted == True:
            print("The patron",patronName,"has been deleted.")
        else:
            print("Unable to find patron")
            
        input("Please enter any key to continue.\n")
        
    def deleteBook(self):
        print("Delete Book")
        print("...........")
        
        bookTitle = str(input("Please enter the book title you wish to delete : "))
        bookDeleted = self._library.deleteBook(bookTitle)
        
        if bookDeleted == True:
            print("the book",bookTitle,"has been deleted.")
        else:
            print("Unable to find book")
        
        input("Please enter any key to continue.\n")
        
    def createTestData(self):
        print("Create Test Data")
        print("................")
        
        self._library.addBook("book1", "book author 1")
        self._library.addBook("book2", "book author 2")
        self._library.addBook("book3", "book author 3")
        self._library.addBook("book4", "book author 4")
        self._library.addBook("book5", "book author 5")
        self._library.addBook("book6", "book author 6")
        self._library.addBook("book7", "book author 7")
        self._library.addBook("book8", "book author 8")
        self._library.addBook("book9", "book author 9")
        self._library.addBook("book10", "book author 10")
        
        self._library.addPatron("Bradley")
        self._library.addPatron("Craig")
        self._library.addPatron("Lauren")
        self._library.addPatron("Heath")
        self._library.addPatron("Kate")
    
def main():
    Manager()
    Manager().showMenu()

main()

    
    
        
                   
                
                
                
            
