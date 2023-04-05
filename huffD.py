#Decode a file using the Huffman algorithm, and a given dictionary.

import os
import sys
import bitstring as bs


def getDictionary(filepath):
    #The syntax of the dictionary file is as follows:
    #character (some number of spaces) binary code

    #Open the file
    file = open(filepath, "r", encoding='utf-8')
    lines = file.readlines()
    file.close()

    dictionary = {}

    #Create a dictionary from the file
    for line in lines:
        #Split the line into the character and the binary code
        splitLine = line.split(" ")
        character = splitLine[0]
        if character == "space":
            character = " "
        if character == "\\n":
            character = str(chr(10))
        if character == "tab":
            character = str(chr(9))
        binaryCode = splitLine[-1].strip()

        #Add the character and binary code to the dictionary
        dictionary[binaryCode] = character
    
    return dictionary

def decodeFile(dictionary, filepath):
    #Open the file
    file = open(filepath, "rb")
    #Using the bitstring library, read the file as a byte array
    binaryCode = bs.BitArray(file.read()).bin
    file.close()

    #Decode the file
    text = []
    currentCharacter = ""
    for bit in binaryCode:
        #Convert the bit to a string
        bitString = str(bit)
        #Add the bit to the current character
        currentCharacter += bitString
        #If the current character is in the dictionary, add it to the text
        if currentCharacter in dictionary:
            text.append(dictionary[currentCharacter])
            currentCharacter = ""
        
    

        
    #Convert the list of characters to a string
    text = "".join(text)

    filename = "./decodings/huff/" + filepath.split("/")[-1].removesuffix(".huff")

    #If the file already exists, overwrite it
    if os.path.exists(filename):
        os.remove(filename)
    
    #Create a text file
    file = open(filename, "w", encoding='utf-8')
    #Write the text to the file
    file.write(text)
    file.close()


def main():
    if len(sys.argv) != 2:
        print("Usage: python huffd.py encodedFile")
        return
    #Get the dictionary
    dictionary = getDictionary("./huffDictionary.txt")
    #Decode the file
    decodeFile(dictionary, sys.argv[1])

if __name__ == "__main__":
    main()
