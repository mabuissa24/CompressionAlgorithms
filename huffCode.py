#This file takes the 12 books, performs a character count, and produces a Huffman code for the aggregate of the 12 books.
#We want our code to produce a minimum variance Huffman code): it just requires to sort super-symbol(s) higher than any symbol of equal (aggregate) probability.
import os
import sys

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.frequency < other.frequency

class HuffmanCoding:
    def importFiles(filepath): #Note, this will read every file in the source directory.
        source = os.listdir(filepath)
        texts = []
        for file in source:
            with open(filepath + file, "r", encoding='utf-8') as f:
                texts.append(f.read())
        return texts

    def countCharacters(texts):
        characters = {}
        for text in texts:
            for character in text:
                #Exclude non-printable characters
                boolean = ord(character) < 33 or ord(character) > 126 and ord(character)
                if boolean:
                    #Switch statement to map utf-8 characters onto their ascii equivalents
                    match ord(character):
                        case 32:
                            character = "space"
                        case 9:
                            character = "tab"
                        case 10:
                            character = "\\n"
                        case 8217:
                            character = "'"
                        case 8216:
                            character = "'"
                        case 8211:
                            character = "-"
                        case 8220:
                            character = '"'
                        case 8221:
                            character = '"'
                        case 8212:
                            character = "-"
                        case 250:
                            character = "u"
                        case 233:
                            character = "e"
                        case 237:
                            character = "i"
                        case 243:
                            character = "o"
                        case 225:
                            character = "a"
                        case _:
                            continue
                    
                if character not in characters:
                    newNode = Node(character, 1)
                    characters[character] = newNode
                else:
                    characters[character].frequency += 1
        return characters

    def sortCharacters(characters):
        #Sort dictionary by value. If the value is the same, sort by length of key.
        sortedCharacters = sorted(characters.values(), key=lambda x: (x.frequency, len(x.character)), reverse=True)
        return sortedCharacters

    def createHuffmanCode(sortedCharacters):
        while len(sortedCharacters) > 1:
            #Get the two lowest frequency characters
            first = sortedCharacters.pop()
            second = sortedCharacters.pop()

            #Create a node for the two characters
            superCharacter = Node(first.character + second.character, first.frequency + second.frequency)
            superCharacter.left = first
            superCharacter.right = second
            #Insert the new super-character into the list
            sortedCharacters.append(superCharacter)
            #Sort the list again
            sortedCharacters = sorted(sortedCharacters, key=lambda x: (x.frequency, len(x.character)), reverse=True)
        return sortedCharacters
    
    def charToCode(huffmanCode):
        dictionary = {}
       
       #Perform a full tree traversal, and add the character to the dictionary
        def traverse(node, code):
            if node.left is None and node.right is None:
                dictionary[node.character] = code
                return
            if node.left is not None:
                traverse(node.left, code + "0")
            if node.right is not None:
                traverse(node.right, code + "1")
        traverse(huffmanCode[0], "")

        return dictionary
        



    def main(self, bookFilepath):

        #First argument is the filepath to the books, i.e "./books/"
        filepath = bookFilepath
        texts = self.importFiles(filepath)

        #Count characters in the books.
        characters = self.countCharacters(texts)
        sortedCharacters = self.sortCharacters(characters)

        #Create the Huffman code
        huffmanCode = self.createHuffmanCode(sortedCharacters)

        #Convert the Huffman code to a dictionary
        charToCode = self.charToCode(huffmanCode)

        #Sort the dictionary by utf-8 code, remember to convert space, tab, and newline to their utf-8 codes. (i.e "space" -> "32")
        charToCode = dict(sorted(charToCode.items(), key=lambda x: 9 if x[0] == "tab" else 10 if x[0] == "\\n" else 32 if x[0] == "space" else ord(x[0])))

        for character in charToCode:
           print(character, "\t", charToCode[character])

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python huffCode.py <bookFilepath>")
        sys.exit(1)
    
    #First argument is the filepath to the books, i.e "./books/"
    bookFilepath = sys.argv[1]
    
    HuffmanCoding.main(HuffmanCoding, bookFilepath)