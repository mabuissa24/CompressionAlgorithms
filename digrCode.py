from collections import Counter
from huffCode import HuffmanCoding as hc
import os
import sys

def countDigrams(texts) -> Counter:
    diFreqs = Counter()
    for text in texts:
        for i in range(len(text) - 1): # note the len(text) - 1 to avoid index error
            d = text[i:i+2]
            if isPrintable(d):
                diFreqs[d] += 1

    return diFreqs

def countUnigrams(texts) -> Counter:
    uniFreqs = Counter()
    for text in texts:
        for u in text:
            if ord(u) >= 32 and ord(u) <= 126:
                uniFreqs[u] += 1
    print(uniFreqs)
    return uniFreqs

def isPrintable(text) -> bool:
    for c in text:
        if ord(c) < 32 or ord(c) > 126:
            return False
    return True

def computeCode(n, texts):
    code = [] # unigrams/digrams are indexed by binary symbols
    for i in range(96):
        pAsc = i + 32
        code.append(chr(pAsc))

    if n == 96:
        return code
    numOfDigrams = n - 96 # number of digrams in our alphabet

    # TODO: need to deal with edge case where len(most_common(numOfDiagrams)) < numOfDiagrams
    commonDigramsTuples = countDigrams(texts).most_common(numOfDigrams)
    assert len(commonDigramsTuples) == numOfDigrams, "TODO: need to deal with edge case where len(most_common(numOfDiagrams)) < numOfDiagrams"

    commonDigrams = sorted([dt[0] for dt in commonDigramsTuples])
    for i in range(numOfDigrams):
        code.append(commonDigrams[i])
    return code

def bitsRequired(n):
    return len(bin(n)[2:])

def getBin(n: int, numOfBits: int):
    return bin(n)[2:].zfill(numOfBits)

def hardBooksCode():
    path = "./books/"
    texts = hc.importFiles(path)
    return computeCode(256, texts)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python digrCode.py <numberOfEntries> <bookFilepath>")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 96:
        print("Number of entries in dictionary must be >= 96")
        sys.exit(1)

    texts = hc.importFiles(sys.argv[2])
    code = computeCode(n, texts)
    numOfBits = bitsRequired(n-1)
    for i in range(len(code)):
        print(f"{getBin(i, numOfBits)}\t{code[i]}")
 
    
