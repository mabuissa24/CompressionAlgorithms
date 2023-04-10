# This file will take a .txt file of binary digits and decode into the original text.
# Specifically, it will build the dictionary in the same method as ZC.py and read through
# the input file, decoding as it goes. It will begin by reading sequences of 7 bits and
# increment this length everytime the dictionary is at max capacity
import math
import sys
import bitstring as bs


def decode(dictionary, text):
    # Initialize dict_ind to size of dictionary, start with minimum code size
    dict_copy = dictionary.copy()
    dict_ind = len(dictionary) + 2
    num_bits = math.ceil(math.log(dict_ind, 2))

    i = 0
    original = []
    next_entry = ""

    # Iterate through the characters in the file and decode them
    while i < len(text):

        flag = False
        index = int(text[i:i + num_bits], 2)
        i = i + num_bits

        if index == 0:
            dictionary = dict_copy.copy()
            dict_ind = len(dictionary) + 2
            num_bits = math.ceil(math.log(dict_ind, 2))
            continue
        elif index == 1:
            # Check our dictionary size at each dictionary element added
            num_bits += 1
            continue
        elif index not in dictionary:
            # print(f"special case at {index}")
            if index != dict_ind:
                print(f"Something went wrong. Hit special case with index {index} of dict index {dict_ind} "
                      f"while text is at index {i} of {len(text)}.")
            flag = True
            letters = next_entry
        else:
            letters = dictionary[index]
        original.append(letters)

        # If our dictionary is full we don't need to add more elements
        if dict_ind >= math.pow(2, 16):
            continue

        # Go through the letters to construct the next entry
        j = 0
        while j < len(letters):
            letter = letters[j]
            next_entry += letter
            # We found the end of the next entry to be added to the dict
            if next_entry not in dictionary.values():
                dictionary[dict_ind] = next_entry
                dict_ind += 1
                if flag:
                    original.append(next_entry[len(letters):])
                    letters = next_entry
                    next_entry = letters[j]

                # We start the next entry with the last letter of the entry we just added
                else:
                    next_entry = letter
            j += 1

    return "".join(original)


def new_dict():
    dictionary = {i - 31 + 1: chr(i) for i in range(32, 128)}
    index = len(dictionary) + 2
    chars = ["\n", "\t"]
    for char in chars:
        dictionary[index] = char
        index += 1
    return dictionary


def main(filename):
    # Dictionary starts with 96 ASCII characters, represented by 7 bits
    dictionary = new_dict()

    # Read the bitstring as one string
    binary = open(filename, "rb").read()
    binary = bs.BitArray(binary).bin

    # Return the decoded version of text
    return decode(dictionary, binary)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python ZD.py <filename>")
        sys.exit(1)

    path = sys.argv[1]
    decoded = main(path)

    with open("decodings/Z/" + sys.argv[1].split("/")[-1].removesuffix(".Z"), "w") as f:
        f.write(decoded)
