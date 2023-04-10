#Concatenate all text files in the books directory into one file, and save it as booksconcatenated.txt
import os

def concatenate():
    #Get all the files in the books directory
    books = os.listdir("./books/")
    #Create a new file
    with open("./books/booksconcatenated.txt", "w", encoding='utf-8') as f:
        #For each file
        for book in books:
            #Open the file
            with open("./books/" + book, "r", encoding='utf-8') as b:
                #Write the contents of the file to the new file
                f.write(b.read())
    #Close the file
    f.close()


if __name__ == "__main__":
    concatenate()