#This file takes the 12 books, performs a character count, and produces a Huffman code for the aggregate of the 12 books.
#We want our code to produce a minimum variance Huffman code): it just requires to sort super-symbol(s) higher than any symbol of equal (aggregate) probability.
import os

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
            if ord(character) < 32 or ord(character) > 126:
                continue

            if character not in characters:
                characters[character] = 1
            else:
                characters[character] += 1
    return characters

def sortCharacters(characters):
    #Sort dictionary by value. If the value is the same, sort by length of key.
    sortedCharacters = sorted(characters.items(), key=lambda x: (x[1], len(x[0])), reverse=True)
    return sortedCharacters

def main():
    filepath = "./books/"
    texts = importFiles(filepath)
    characters = countCharacters(texts)
    sortedCharacters = sortCharacters(characters)
    print(sortedCharacters)

if __name__ == "__main__":
    main()