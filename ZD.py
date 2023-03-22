# This file will take a .txt file of binary digits and decode into the original text.
# Specifically, it will build the dictionary in the same method as ZC.py and read through
# the input file, decoding as it goes. It will begin by reading sequences of 7 bits and
# increment this length everytime the dictionary is at max capacity

import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python ZD.py <filename>")
        sys.exit(1)

    path = sys.argv[1]
    print("To be implemented")
