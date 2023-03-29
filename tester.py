import ZC, ZD


def Z_test_encode():
    # Test dictionary
    dictionary = {" ": 1, "a": 2, "b": 3, "o": 4, "w": 5}

    # Just one character
    unencoded = "a"
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct = "0000010"
    assert encoded == correct, f"Encoded \"{unencoded}\" as {encoded} instead of {correct}"

    # Multiple characters, no repetition
    unencoded = "wa "
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct = "000010100000100000001"
    assert encoded == correct, f"Encoded \"{unencoded}\" as {encoded} instead of {correct}"

    # Multiple characters with repetition
    unencoded = "wabba wabba wabba wabba woo woo woo"
    encoded = ZC.encode(dictionary.copy(), unencoded)
    correct_list = [5, 2, 3, 3, 2, 1, 6, 8, 10, 12, 9, 11, 7, 16, 5, 4, 4, 11, 21, 23, 4]
    correct_list_binary = [format(x, "b").zfill(7) for x in correct_list]
    correct = "".join(correct_list_binary)
    assert encoded == correct, f"Encoded \"{unencoded}\" as {encoded} instead of {correct}"


def test_decode(algo):
    match algo:
        case "Z":
            print("Testing algorithm Z decoder, to be implemented")
            encoded = None
            decoded = None
            # correct = "wabba wabba wabba wabba woo woo woo"
            # assert decoded == correct, f"Decoded {decoded} instead of {correct}"
        case "digrXXX":
            encoded = None
        case "huff":
            encoded = None


if __name__ == "__main__":
    Z_test_encode()
    test_decode("Z")
