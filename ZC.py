# This file will encode with a changing dictionary. It starts with the alphabet (96 ascii chars)
# and adds code words as it reads through the input file. The code words will begin with length 7.
# At each step, it sends the longest sequence of chars that's currently in the dictionary, and
# adds one more entry to the dictionary that includes the entry just used concat with the next char.
# Once the dict is full (max #bits = 16) it will monitor compression rate and when it dips below
# a certain threshold it'll flush the dictionary and rebuild it

import sys


def main(filename):
    # Dictionary starts with 96 ASCII characters
    dictionary = {chr(i): i - 31 for i in range(32, 128)}
    dict_ind = 127

    # Read the file as one string
    with open("" + filename, "r", encoding='utf-8') as f:
        text = f.read()

    # Iterate through the characters in the file and encode
    i = 0
    while i < len(text):
        j = i
        # Look for the longest string of characters already in dictionary
        string = text[i]
        while j < len(text):
            # If we find something not in the dictionary, add it and return its code
            if string + text[j] not in dictionary:
                dictionary[string + text[j]] = dict_ind
                dict_ind += 1
                code = dictionary[string]
                # Add code represented by correct number of bits

            else:  # Otherwise, add the character to the string that we can transmit
                string = string + text[j]

        # Build dictionary with the max string found + next char
        return
    return


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python ZC.py <filename>")
        sys.exit(1)

    path = sys.argv[1]
    main(path)
