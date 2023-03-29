#Using a set dictionary, generate a compressed file.


import sys


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
        binaryCode = splitLine[-1].strip()

        if character == "space":
            character = " "
        if character == "\\n":
            character = str(chr(10))
        if character == "tab":
            character = str(chr(9))
        #Add the character and binary code to the dictionary
        dictionary[character] = binaryCode
    
    return dictionary

def compressFile(filepath, dictionary):
    #Open the file
    file = open(filepath, "r", encoding='utf-8')
    text = file.read()
    file.close()

    filename = filepath.split("/")[-1]
    #Create a binary file
    file = open("./encodings/" + filename+ ".huff", "wb")


    #Encode the file
    for character in text:
        #Exclude non-printable characters
        if ord(character) < 32 or ord(character) > 126:
            continue

        #Get the binary code for the character
        binaryCode = dictionary[character]

        #Convert the binary code to a sequence of bits
        bits = []
        for bit in binaryCode:
            bits.append(int(bit))
        
        #Write the bits to the file
        for bit in bits:
            file.write(bit.to_bytes(1, byteorder='big'))
        

    file.close()

def main():
    #Usage: python huffCode.py <filepath>
    if len(sys.argv) < 2:
        print("Usage: python huffCode.py <filepath>")
        return

    #Get the filepath
    filepath = sys.argv[1]

    #Get the dictionary
    dictionary = getDictionary("./huffDictionary.txt")

    #Compress the file
    compressFile(filepath, dictionary)

if __name__ == "__main__":
    main()
