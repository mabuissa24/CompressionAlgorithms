import ZC, ZD


def Z_test_encode():
    # Test dictionary
    dictionary = {" ": 2, "a": 3, "b": 4, "o": 5, "w": 6}

    # Just one character
    unencoded = "a"
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct = "011"
    assert encoded == correct, f"Encoded \"{unencoded}\" as {encoded} instead of {correct}"

    # Multiple characters, no repetition
    unencoded = "wa "
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct = "11000100110010"
    assert encoded == correct, f"Encoded \"{unencoded}\" as {encoded} instead of {correct}"

    # Multiple characters with repetition
    unencoded = "wabba wabba wabba wabba woo woo woo"
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct_list = [5, 0, 2, 3, 3, 2, 1, 6, 8, 10, 0, 12, 9, 11, 7, 16, 5, 4, 4, 11, 21, 23, 4]
    correct_list = [i + 1 for i in correct_list]
    correct_list_binary = [format(x, "b").zfill(3) for x in correct_list[:2]]
    correct_list_binary += [format(x, "b").zfill(4) for x in correct_list[2:11]]
    correct_list_binary += [format(x, "b").zfill(5) for x in correct_list[11:]]
    correct = "".join(correct_list_binary)
    assert encoded == correct, f"Encoded \"{unencoded}\" as \n{encoded} \n{correct}"

    # Special case when decoding
    dictionary = {"a": 2, "b": 3}
    unencoded = "abababa"
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct = "01010011100110"
    assert encoded == correct, f"Encoded \"{unencoded}\" as {encoded} instead of {correct}"


def test_decode(algo):
    match algo:
        case "Z":
            encode_dictionary = {" ": 2, "a": 3, "b": 4, "o": 5, "w": 6}
            decode_dictionary = {2: " ", 3: "a", 4: "b", 5: "o", 6: "w"}
            # Short string
            unencoded = "waw"
            encoded = ZC.encode(encode_dictionary.copy(), unencoded)
            # print(encoded)
            decoded = ZD.decode(decode_dictionary.copy(), encoded)
            assert decoded == unencoded, f"Decoded {decoded} instead of {unencoded}"
            # Longer string
            unencoded = "wabba"
            encoded = ZC.encode(encode_dictionary.copy(), unencoded)
            decoded = ZD.decode(decode_dictionary.copy(), encoded)
            assert decoded == unencoded, f"Decoded {decoded} instead of {unencoded}"
            # Long string
            unencoded = "wabba wabba wabba wabba woo woo woo"
            encoded = ZC.encode(encode_dictionary.copy(), unencoded)
            decoded = ZD.decode(decode_dictionary.copy(), encoded)
            assert decoded == unencoded, f"Decoded {decoded} instead of {unencoded}"
            # Special case as listed in book
            encode_dictionary = {"a": 2, "b": 3}
            decode_dictionary = {2: "a", 3: "b"}
            unencoded = "ababababababa"
            encoded = ZC.encode(encode_dictionary.copy(), unencoded)
            decoded = ZD.decode(decode_dictionary.copy(), encoded)
            assert decoded == unencoded, f"Decoded {decoded} instead of {unencoded}"

            encode_dictionary = ZC.new_dict()
            decode_dictionary = ZD.new_dict()
            unencoded = "tgwww.www."
            encoded = ZC.encode(encode_dictionary.copy(), unencoded)
            print(f"encoded is {encoded}")
            decoded = ZD.decode(decode_dictionary.copy(), encoded)
            print(f"decoded is {decoded}")
            assert decoded == unencoded, f"Decoded {decoded} instead of {unencoded}"

            # Issue in book
            encode_dictionary = ZC.new_dict()
            decode_dictionary = ZD.new_dict()
            unencoded = """The Project Gutenberg eBook of Trials of war criminals before the
Nuernberg military tribunals under control council law no. 10, by
Anonymous

This eBook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this eBook or online at
www.gutenberg.org. If you are not located in the United States, you
will have to check the laws of the country where you are located before
using this eBook.

Title: Trials of war criminals before the Nuernberg military tribunals
       under control council law no. 10

Author: Anonymous

Release Date: March 21, 2023 [eBook #70342]

Language: English

Produced by: Emmanuel Ackerman, Karin Spence and the Online Distributed
             Proofreading Team at https://www.pgdp.net (This file was
             produced from images generously made available by The
             Internet Archive)
"""

            encoded = ZC.encode(encode_dictionary.copy(), unencoded)
            decoded = ZD.decode(decode_dictionary.copy(), encoded)
            # print(f"decoded is {decoded}")
            assert decoded == unencoded, f"Decoded {decoded} instead of {unencoded}"

        case "digrXXX":
            encoded = None
        case "huff":
            encoded = None


if __name__ == "__main__":
    Z_test_encode()
    test_decode("Z")
