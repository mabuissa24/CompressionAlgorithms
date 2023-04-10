# README

To run any digram encoding algorithm, the python library `bitstring` is required.

    $ pip install bitstring

## Encoding

To run any of the encoding algorithms, run the following command:

    $ python <algo>C.py "inputfile.txt"

The output will be written to `./encodings/<algo>/inputfile.txt.<algo>`.

## Decoding

To run any of the decoding algorithms, run the following command:

    $ python <algo>D.py "inputfile.txt.<algo>"

The output will be written to `./decodings/<algo>/inputfile.txt`.

## Evaluation

evaluation.py is available to produce tables for the compression ratios, encoding time, and decoding time of each algorithm. 

By default, it will run the algorithms on all files in the `./books/` directory.

To run it, run the following command:

    $ python evaluation.py

The output will be written to the directory of evaluation.py.

