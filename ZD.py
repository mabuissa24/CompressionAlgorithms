# This file will take a .txt file of binary digits and decode into the original text.
# Specifically, it will build the dictionary in the same method as ZC.py and read through
# the input file, decoding as it goes. It will begin by reading sequences of 7 bits and
# increment this length everytime the dictionary is at max capacity
import math
import sys


def decode(dictionary, text):
    # print(dictionary)
    # print(len(dictionary))
    dict_copy = dictionary.copy()
    # Initialize dict_ind to size of dictionary, start with minimum code size
    dict_ind = len(dictionary) + 2
    num_bits = math.ceil(math.log(dict_ind, 2))

    i = 0
    original = ""
    next_entry = ""

    received = []

    # Iterate through the characters in the file and decode them
    while i < len(text):

        flag = False
        index = int(text[i:i + num_bits], 2)
        # print(f"ZD dictionary is {dictionary} with index {index}")
        print(f"{index}:{dict_ind}:{num_bits}")
        received.append(f"{index}:{dict_ind}:{num_bits}")
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
            print(f"special case at {index}")
            if index != dict_ind:
                print(f"Something went wrong. Hit special case with index {index} of dict index {dict_ind} "
                      f"while text is at index {i} of {len(text)}.")
                # exit(1)
            flag = True
            letters = next_entry
        else:
            letters = dictionary[index]
        original += letters
        # Go through the letters to construct the next entry

        for letter in letters:
            next_entry += letter
            print(f"letters is {letters} and next_entry is {next_entry} at ind {dict_ind}")
            # We found the end of the next entry to be added to the dict
            if next_entry not in dictionary.values():
                dictionary[dict_ind] = next_entry
                dict_ind += 1
                if flag:
                    original += next_entry[len(letters):]
                    # letters += next_entry[len(letters):]
                    print(f"added {next_entry[len(letters):]} to {original}")
                    next_entry = next_entry[len(next_entry) - 1]


                # We start the next entry with the last letter of the entry we just added
                else:
                    next_entry = letter

    print(received)
    print(dictionary)
    print(len(dictionary))

    # print(f"ZD dictionary is {dictionary}")
    return original  # TODO: They don't make the same dictionaries currently.
    # Specifically, in the special case, they don't create the correct NEXT entry (see 102 and 103 in tester.py)


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
    decoded = main(path)

    with open(sys.argv[1].split("/")[-1].removesuffix(".Z"), "w") as f:
        f.write(decoded)
