# This file will take a .txt file of binary digits and decode into the original text.
# Specifically, it will build the dictionary in the same method as ZC.py and read through
# the input file, decoding as it goes. It will begin by reading sequences of 7 bits and
# increment this length everytime the dictionary is at max capacity
import math
import sys


def decode(dictionary, text):
    # Initialize dict_ind to size of dictionary, start with minimum code size
    dict_ind = len(dictionary) + 1
    num_bits = math.ceil(math.log(dict_ind, 2))

    i = 0
    original = ""
    next_entry = ""

    # Iterate through the characters in the file and decode them
    while i < len(text):
        flag = False
        index = int(text[i:i + num_bits], 2)
        i = i + num_bits
        if index == 0:
            dictionary = new_dict()
            dict_ind = len(dictionary) + 1
            num_bits = math.ceil(math.log(dict_ind, 2))
        elif index not in dictionary:
            if index != dict_ind:
                print(f"Something went wrong. Hit special case with index {index} while dict is at index {dict_ind}.")
                exit(1)
            flag = True
            letters = next_entry
        else:
            letters = dictionary[index]
        original += letters
        # Go through the letters to construct the next entry
        for letter in letters:
            next_entry += letter
            # We found the end of the next entry to be added to the dict
            if next_entry not in dictionary.values():
                if flag:
                    original += next_entry[len(letters):]
                dictionary[dict_ind] = next_entry
                dict_ind += 1

                # We start the next entry with the last letter of the entry we just added
                next_entry = letter
            # Check our dictionary size at each dictionary element added
            if dict_ind + 1 >= math.pow(2, num_bits):
                num_bits += 1


        # TODO: Once we reach 16 bits, stop adding, flush dictionary and send code 0 if it compression rate too low

    return original


def new_dict():
    dictionary = {i - 31: chr(i) for i in range(32, 128)}
    index = len(dictionary) + 1
    chars = ["\n", "\t"]
    for char in chars:
        dictionary[index] = char
        index += 1
    return dictionary

def main(filename):
    # Dictionary starts with 96 ASCII characters, represented by 7 bits
    dictionary = new_dict()

    # Read the file as one string
    with open("" + filename, "r", encoding='utf-8') as f:
        text = f.read()

    # Return the decoded version of text
    return decode(dictionary, text)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python ZD.py <filename>")
        sys.exit(1)

    path = sys.argv[1]
    main(path)
