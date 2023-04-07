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

    # Decode the first letter to build upon to make the dictionary
    index = int(text[0:num_bits], 2)
    if index not in dictionary:
        print(f"Something broke. Index {index} wasn't in dictionary")
        exit(1)
    original = dictionary[index]
    next_entry = original
    if next_entry not in dictionary.values():
        print(f"Something broke. The first entry: {next_entry} was not in the original dictionary: {dictionary}")
        exit(1)
    i = num_bits
    print(f"original is {original}")

    # Iterate through the characters in the file and decode them
    while i < len(text):
        index = int(text[i:i + num_bits], 2)
        # print(f"index is {index}")
        if index not in dictionary:
            print("Special case. To be implemented")
            exit(1)
        letters = dictionary[index]
        original += letters
        # Go through the letters to construct the next entry
        for letter in letters:
            next_entry += letter
            # We found the end of the next entry to be added to the dict
            if next_entry not in dictionary.values():
                dictionary[dict_ind] = next_entry
                dict_ind += 1
                print(dictionary)
                # Check our dictionary size at each dictionary element added
                if dict_ind + 1 >= math.pow(2, num_bits):
                    print("increasing num_bits")
                    num_bits += 1
                # We start the next entry with the last letter of the entry we just added
                next_entry = letter

        # for j in range(len(letters)):
        #     if next_entry not in dictionary.values():
        #         dictionary[dict_ind] = next_entry
        #         dict_ind += 1
        #         if len(letters) == j + 1:
        #             next_entry = ""
        #         else:
        #             leftover = letters[j + 1:]
        #             next_entry = leftover[0]
        #             backlog = leftover[1:]
        #         break
        #
        #     next_entry += letters[j]

        # print(dictionary)
        # print(dict_ind)
        # print(dictionary[dict_ind])
        i = i + num_bits
        print(f"original is {original}")


        # binary_code, j = ZC.find_codeword(dictionary, dict_ind, num_bits, i, text)
        # TODO: Once we reach 16 bits, stop adding, flush dictionary and send code 0 if it compression rate too low
        # If dict_ind goes above 2^num_bits, update numbits

    return original


def main(filename):
    # Dictionary starts with 96 ASCII characters, represented by 7 bits
    dictionary = {i - 31: chr(i) for i in range(32, 128)}

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
    print("To be implemented")
