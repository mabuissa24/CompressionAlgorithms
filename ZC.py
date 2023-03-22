# This file will encode with a changing dictionary. It starts with the alphabet (96 ascii chars)
# and adds code words as it reads through the input file. The code words will begin with length 7.
# At each step, it sends the longest sequence of chars that's currently in the dictionary, and
# adds one more entry to the dictionary that includes the entry just used concat with the next char

import sys


def main(filename):
    dictionary = dict()

    # Read the file as one string
    with open("" + filename, "r", encoding='utf-8') as f:
        text = f.read()

    # Iterate through the characters in the file and encode
    for char in text:
        # Look for this character in the dictionary. If it exists, look for this char and the next
        # Build dictionary with the max string found + next char
        return
    return


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python ZC.py <filename>")
        sys.exit(1)

    path = sys.argv[1]
    main(path)
