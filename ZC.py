# This file will encode with a changing dictionary. It starts with the alphabet (96 ascii chars)
# and adds code words as it reads through the input file. The code words will begin with length 7.
# At each step, it sends the longest sequence of chars that's currently in the dictionary, and
# adds one more entry to the dictionary that includes the entry just used concat with the next char.
# Once the dict is full (max #bits = 16) it will monitor compression rate and when it dips below
# a certain threshold it'll flush the dictionary and rebuild it
import math
import sys


def encode(dictionary, text):
    # Initialize dict_ind to size of dictionary, start with codes of minimum possible size
    dict_ind = len(dictionary) + 1
    num_bits = math.ceil(math.log(dict_ind, 2))
    # Iterate through the characters in the file and encode them
    i = 0
    code = ""
    while i < len(text):
        # Look for the longest string of characters already in dictionary
        string = text[i]
        j = i + 1
        while j < len(text):
            new_string = string + text[j]
            # If new string is already in the dictionary, update the string to continue searching
            if new_string in dictionary:
                string = new_string
                j += 1
            # Once we find something not in the dictionary, add it to dictionary and break
            else:
                dictionary[new_string] = dict_ind
                dict_ind += 1
                break

        # Add index from dictionary to the code, represented by correct number of bits
        ind = dictionary[string]
        binary_code = format(ind, "b").zfill(num_bits)
        code += binary_code

        # Update i to point to the last not encoded letter
        i = j

        # If dict_ind goes above 2^num_bits, update numbits
        if dict_ind >= math.pow(2, num_bits):
            num_bits += 1

        # TODO: Once we reach 16 bits, stop adding, flush dictionary and send code 0 if it compression rate too low

    return code


def main(filename):
    # Dictionary starts with 96 ASCII characters, represented by 7 bits
    dictionary = {chr(i): i - 31 for i in range(32, 128)}

    # Read the file as one string
    with open("" + filename, "r", encoding='utf-8') as f:
        text = f.read()

    # Return the encoded version of text
    return encode(dictionary, text)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python ZC.py <filename>")
        sys.exit(1)

    path = sys.argv[1]
    main(path)
