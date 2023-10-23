import pandas as pd  

class Library:
    books=[]
    authers=[]
    def addBook(self,name,auther):
        book= Book(name,auther)
        self.books.append(book)
        return self.books.index(book)
    def addAuther(self,name,email):
        auther= Auther(name,email)
        self.authers.append(auther)
        return self.authers.index(auther)
class Book:
    def __init__(self, name, auther):
      self.name = name
      self.auther =auther

    
    
class Auther:
    def __init__(self, name, email):
        self.name = name
        self.email =email


    
    
library=Library()
inputPromt=0
while(1):
    print("\nWelcome to library managment tool\n")
    print("Here are some of option available\n")
    print("1. Add Auther")
    print("2. Add Book")
    print("3. Delete book at index")
    print("4. Delete auther at index")
    print("5. Find book by auther")
    print("6. Find auther by name")
    print("7. Export library")
    inputPromt = int(input("Enter index of function to perform\n"))
    print(inputPromt)
    if(inputPromt==1):
        name =input("Enter name of auther");
        email =input("Enter email of auther");
        autherIndex=library.addAuther(name,email)
        print(f"Auther added at index {str(autherIndex)}")
    elif(inputPromt==2):
        name =input("Enter name of book");
        autherAdd =input("Enter index or name of auther");
        indexOfAuther=0
        print(autherAdd)
        isNumeric=autherAdd.isnumeric();
        if((not isNumeric)):
            email =input("Enter email of auther");
            indexOfAuther=library.addAuther(autherAdd,email)
        else:
            indexOfAuther=int(autherAdd)
        indexOfBook=library.addBook(name,library.authers[indexOfAuther])
        print(f"Book is add on index {indexOfBook}\n")    
    elif(inputPromt==3):
        indexOfBookToRemove =input("Enter index of book");
        library.books.pop(indexOfBookToRemove)
        print("book removed sucessfully")
    elif(inputPromt==4):
        indexOfAutherToRemove =input("Enter index of auther");
        library.authers.pop(indexOfAutherToRemove)
        print("auther removed sucessfully")
    elif(inputPromt==5):
        keyToSearch =input("Enter key to search book");
        for book in library.books:
            if(keyToSearch in book.name):
                indexOfBook=library.books.index(book)
                print(f"Book found at index {indexOfBook}")
    elif(inputPromt==6):
        keyToSearch =input("Enter key to search auther");
        for aurther in library.authers:
            if(keyToSearch in aurther.name):
                indexOfBook=library.authers.index(book)
                print(f"Book found at index {indexOfBook}")
    elif(inputPromt==7):
        listData=[]
        if(len(library.books)==0):
            print("Library is empty")
        else:   
            for book in library.books:
                listData.append([book.name,book.auther.name,book.auther.email])
            df = pd.DataFrame(listData);
            df.to_csv('filename.csv', index=False,header=["book_name","auther_name","auther_email"])
    inputContinue=input("Want to continue[y/n]")
    if(inputContinue is 'n'):
        break
    else:
        continue
        
        
            
        
            
            
            
            
            

        
        
        
        
        
    
    
    
    
       
        
    
    