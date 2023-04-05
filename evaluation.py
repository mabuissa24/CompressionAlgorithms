import os 
import sys
import time

Algorithms = ["huff", "digr256", "digr512", "digr1024"]

def evaluate():
    books = os.listdir("./books/")

    #Produce 3 tables, one for each of the following: compression ratio, compression time, decompression time.
    #Each table will have 5 columns, one for each algorithm, and a row for each book.

    numberOfBooks = len(books)

    #Compression ratio
    compressionTable = [[0 for i in range(len(Algorithms))] for j in range(numberOfBooks)]
    #Compression time
    compressionTimeTable = [[0 for i in range(len(Algorithms))] for j in range(numberOfBooks)]
    #Decompression time
    decompressionTimeTable = [[0 for i in range(len(Algorithms))] for j in range(numberOfBooks)]

    #For each book
    for book in books:
        #For each algorithm
        for algorithm in Algorithms:
            #Get the compression time
            compressionTimeTable[books.index(book)][Algorithms.index(algorithm)] = getCompressionTime(book, algorithm)
            #Get the decompression time
            decompressionTimeTable[books.index(book)][Algorithms.index(algorithm)] = getDecompressionTime(book, algorithm)
            #Get the compression ratio
            compressionTable[books.index(book)][Algorithms.index(algorithm)] = getCompressionRatio(book, algorithm)
        
    #Save the tables as .csv files, with titles
    saveTable(compressionTable, "Compression Ratio")
    saveTable(compressionTimeTable, "Compression Time")
    saveTable(decompressionTimeTable, "Decompression Time")

def getCompressionRatio(book, algorithm):
    #Get the size of the original file
    originalSize = os.path.getsize("./books/" + book)
    #Get the size of the compressed file
    compressedSize = os.path.getsize("./encodings/"+algorithm + "/" + book + "." + algorithm)
    #Return the ratio
    return compressedSize / originalSize

def getCompressionTime(book, algorithm):
    #Get the time before compression
    start = time.time()
    #Compress the file
    os.system("python " + algorithm + "C.py ./books/" + book)
    #Get the time after compression
    end = time.time()
    #Return the difference
    return end - start

def getDecompressionTime(book, algorithm):
    #Get the time before decompression
    start = time.time()
    #Decompress the file
    os.system("python " + algorithm + "D.py ./encodings/"+algorithm + "/" + book + "." + algorithm)
    #Get the time after decompression
    end = time.time()
    #Return the difference
    return end - start

def saveTable(table, title):
    books = os.listdir("./books/")
    #Open the file
    with open(title + ".csv", "w") as f:
        #Write the first row to be the titles
        f.write("Book," + ",".join(Algorithms) + ","+ "\n")
        #For each book
        for row in table:
            #Write the book name
            f.write(books[table.index(row)] + ",")
            #For each algorithm
            for column in row:
                #Write the value
                f.write(str(column) + ",")
            #Go to the next line
            f.write("\n")
        
def main():
    evaluate()

if __name__ == "__main__":
    main()
