from collections import Counter
from huffCode import HuffmanCoding as hc
import os
import sys

def countDigrams(texts: list) -> Counter:
    """
    @param
    texts: list of strings

    Counts the number of digrams in texts.
    Only counts printable digrams.

    @return
    diFreqs: Counter() object of digrams
    """
    diFreqs = Counter()
    for text in texts:
        for i in range(len(text) - 1): # note the len(text) - 1 to avoid index error
            d = text[i:i+2]
            if isPrintable(d):
                diFreqs[d] += 1

    return diFreqs

def isPrintable(text) -> bool:
    """
    Determines if a text contains only printable characters.
    """
    for c in text:
        if ord(c) < 32 or ord(c) > 126:
            return False
    return True

def computeCode(n : int, texts: list) -> list:
    """
    @param
    n : number of entries in code.
    texts: list of strings

    Computes a code structured as follows:
    First 96 entries: printable unigrams
    Rest of the entries: most common n - 96 digrams in ascending order

    @return

    code : list

    Note that we return a list instead of a dictionary because all codewords
    are of the same length. As such, we can compute the appropriate binary
    code word with an index and the number of entries in the code.
    """

    if n < 96:
        raise Exception("Code must be at least n=96 entries long!")

    code = [] # unigrams/digrams are indexed by binary symbols
    for i in range(96):
        printableUnigram = i + 32
        code.append(chr(printableUnigram))

    if n == 96:
        return code
    
    numOfDigrams = n - 96 # number of digrams we would LIKE in our alphabet
    commonDigramsTuples = countDigrams(texts).most_common(numOfDigrams)
    # note that there might not be enough digrams to fill out all n entries of code!
    # In this case, len(commonDigramTuples) < n- 96 and we return a shorter code.

    commonDigrams = sorted([dt[0] for dt in commonDigramsTuples])
    for cd in commonDigrams:
        code.append(cd)
    return code

def bitsRequired(n : int):
    """
    Number of bits needed to represent an int n
    in binary
    """
    return len(bin(n)[2:])

def getBin(n: int, numOfBits: int):
    """
    Get binary representation of n using numOfBits bits.
    Does not test whether numOfBits are enough bits.
    """
    return bin(n)[2:].zfill(numOfBits)

def hardBooksCode():
    path = "./books/"
    texts = hc.importFiles(path)
    return computeCode(256, texts)

 



if __name__ == "__main__":
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Usage: python digrCode.py <numberOfEntries> <bookFilepath> [writeToFileBool]")
        sys.exit(1)

    writeToFile = False
    if len(sys.argv) == 4:
        if sys.argv[3] == "True":
            writeToFile = True
        elif sys.argv[3] == "False":
            writeToFile = False
        else:
            print("Usage: python digrCode.py <numberOfEntries> <bookFilepath> [writeToFileBool]")
            print("Note that [writeToFileBool] should be either 'True' or 'False'")
            sys.exit(1)

    n = int(sys.argv[1])
    if n < 96:
        print("Number of entries in dictionary must be >= 96")
        sys.exit(1)
    
    texts = hc.importFiles(sys.argv[2])
    code = computeCode(n, texts)
    m = len(code)
    fullCode = True if (m==n) else False
    numOfBits = bitsRequired(m-1)

    codeFile = None
    if writeToFile:
        if not os.path.exists('digrCodes'):
            os.makedirs('digrCodes')
        codeFile = open(f"digrCodes/digrCode{m}.txt", "w")
    
    for i in range(m):
        if codeFile:
            codeFile.write(f"{getBin(i, numOfBits)}\t{code[i]}\n")
        print(f"{getBin(i, numOfBits)}\t{code[i]}")
    if not fullCode:
        print(f"WARNING: not enough digrams to construct a {n}-element code.\n")
    if codeFile:
        print(f"Output written on digrCodes/digrCode{m}.txt")
    
 
    
