import ZC, ZD


def Z_test_encode():
    # Test dictionary
    dictionary = {" ": 1, "a": 2, "b": 3, "o": 4, "w": 5}

    # Just one character
    unencoded = "a"
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct = "010"
    assert encoded == correct, f"Encoded \"{unencoded}\" as {encoded} instead of {correct}"

    # Multiple characters, no repetition
    unencoded = "wa "
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct = "1010100001"
    assert encoded == correct, f"Encoded \"{unencoded}\" as {encoded} instead of {correct}"

    # Multiple characters with repetition
    unencoded = "wabba wabba wabba wabba woo woo woo"
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct_list = [5, 2, 3, 3, 2, 1, 6, 8, 10, 12, 9, 11, 7, 16, 5, 4, 4, 11, 21, 23, 4]
    correct_list_binary = [format(x, "b").zfill(3) for x in correct_list[:2]]
    correct_list_binary += [format(x, "b").zfill(4) for x in correct_list[2:10]]
    correct_list_binary += [format(x, "b").zfill(5) for x in correct_list[10:]]
    correct = "".join(correct_list_binary)
    assert encoded == correct, f"Encoded \"{unencoded}\" as {encoded} instead of {correct}"


def test_decode(algo):
    match algo:
        case "Z":
            encode_dictionary = {" ": 1, "a": 2, "b": 3, "o": 4, "w": 5}
            decode_dictionary = {1: " ", 2: "a", 3: "b", 4: "o", 5: "w"}
            # Short string
            unencoded = "waw"
            encoded = ZC.encode(encode_dictionary.copy(), unencoded)
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
            encode_dictionary = {"a": 1, "b": 2}
            decode_dictionary = {1: "a", 2: "b"}
            unencoded = "abababababababa"
            encoded = ZC.encode(encode_dictionary.copy(), unencoded)
            decoded = ZD.decode(decode_dictionary.copy(), encoded)
            assert decoded == unencoded, f"Decoded {decoded} instead of {unencoded}"


        case "digrXXX":
            encoded = None
        case "huff":
            encoded = None


if __name__ == "__main__":
    Z_test_encode()
    test_decode("Z")
