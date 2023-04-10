# This file will encode with a changing dictionary. It starts with the alphabet (96 ascii chars)
# and adds code words as it reads through the input file. The code words will begin with length 7.
# At each step, it sends the longest sequence of chars that's currently in the dictionary, and
# adds one more entry to the dictionary that includes the entry just used concat with the next char.
# Once the dict is full (max #bits = 16) it will monitor compression rate and when it dips below
# a certain threshold it'll flush the dictionary and rebuild it
import math
import sys
import bitstring as bs


def encode(dictionary, text):
    dict_copy = dictionary.copy()

    utf_dict = {"’".encode('utf-8'): "'", "“".encode('utf-8'): '"', "á".encode('utf-8'): 'a',
                "é".encode('utf-8'): "e", "ó".encode('utf-8'): "o", "—".encode('utf-8'): "-",
                "‘".encode('utf-8'): "'", "”".encode('utf-8'): '"', "í".encode('utf-8'): "i"}
    # Initialize dict_ind to size of dictionary, start with codes of minimum possible size
    dict_ind = len(dictionary) + 2
    num_bits = math.ceil(math.log(dict_ind, 2))
    # Iterate through the characters in the file and encode them
    i = 0
    code = ""
    flag = False
    while i < len(text):
        # If dict_ind goes above 2^num_bits, update numbits
        if dict_ind >= math.pow(2, num_bits) and not flag:
            # Once we finish 16 bits, stop adding, flush dictionary and send code 0 if compression rate too low
            if num_bits == 16:
                flag = True
                code_start = len(code)
                text_start = i
            else:
                binary_code = format(1, "b").zfill(num_bits)
                code += binary_code
                num_bits += 1
                continue
        # Look for the longest string of characters already in dictionary
        string = text[i]
        if string in utf_dict:
            string = utf_dict[string]
        elif string not in dictionary:
            string = "*"
        j = i + 1
        while j < len(text):
            char = text[j]
            if char in utf_dict:
                char = utf_dict[text[j]]
            elif char not in dictionary:
                char = "*"
            new_string = string + char
            # If new string is already in the dictionary, update the string to continue searching
            if new_string in dictionary:
                string = new_string
                j += 1
            # Once we find something not in the dictionary, add it to dictionary and break
            elif not flag:
                dictionary[new_string] = dict_ind
                dict_ind += 1
                break
            else:
                break

        # Add index from dictionary to the code, represented by correct number of bits
        ind = dictionary[string]
        binary_code = format(ind, "b").zfill(num_bits)
        code += binary_code

        if flag:
            # Calculate compression ratio
            ratio = 8 * (j - text_start) / (len(code) - code_start)
            if ratio < 2.7 and j - text_start > 100:
                binary_code = format(0, "b").zfill(num_bits)
                code += binary_code
                dictionary = dict_copy.copy()
                dict_ind = len(dictionary) + 1
                num_bits = math.ceil(math.log(dict_ind, 2))
                flag = False
                continue

        # Update i to point to the last not encoded letter
        i = j

    return code


def new_dict():
    dictionary = {chr(i): i - 31 + 1 for i in range(32, 128)}
    index = len(dictionary) + 2
    chars = ["\n", "\t"]
    for char in chars:
        dictionary[char] = index
        index += 1
    return dictionary


def main(filename):
    # Dictionary starts with 96 ASCII characters, represented by 7 bits
    dictionary = new_dict()

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
    name = path.split("/")[-1]
    encoded = main(path)

    #Translate the encoded string into a bitstring
    bitstring = bs.BitArray(bin=encoded)

    # Write the bitstring to a file
    with open("./encodings/Z/" + name + ".Z", "wb") as f:
        bitstring.tofile(f)
    