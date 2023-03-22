from collections import Counter
import huffCode as hC
import os
import sys

def countDigrams(texts):
    digrams = Counter()
    for text in texts:
        for i in range(len(texts)):
            d = text[i:i+2]
            if isPrintable(d):
                digrams[d] += 1
    return digrams

def countUnigrams(texts):
    unigrams = Counter()
    for text in texts:
        for u in text:
            if ord(u) >= 32 and ord(u) <= 126:
                unigrams[u] += 1
    return unigrams

def isPrintable(text):
    for c in text:
        if ord(c) < 32 or ord(c) > 126:
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python digrCode.py <numberOfEntries> <bookFilepath>")
        sys.exit(1)
    if sys.argv[1] < 96:
        print("Number of entries in dictionary must be >= 96")
        sys.exit(1)

    print("to be implemented")
    
