import bitstring as bs
import digrCode as dc
import os

class CodeDoubleMap:
    """
    A double dictionary of sorts, used to index into both codewords and symbols
    """
    def __init__(self, codeArray: list):
        """
        @param
        codeArray : list -> code in list form (each entry is a symbol, indices of list represent codewords.

        Constructs reverseMap (symbols -> int codewords) from codeArray.
        """
        self.reverseMap = {} # keys: symbols; values: int codewords
        self.codeArray = codeArray
        self.codewordLen = dc.bitsRequired(len(codeArray) - 1) # number of bits per codeword
        for i in range(len(codeArray)):
            self.reverseMap[codeArray[i]] = i

    def getSymbol(self, codeWord: int):
        return self.codeArray[codeWord]

    def getIntCodeword(self, symbol):
        """
        Get int codeword. 
        """
        try:
            codeWord = self.reverseMap[symbol]
            return codeWord
        except KeyError:
            return None

class DigramCompression:
    """
    Main tool used for digram compression and decompression.
    """
    def __init__(self, codeSize: int):
        """
        @param
        codeSize -> only supports 256, 512, and 1024
        
        Loads a code from directory './digrCodes/' and constructs a CodeDoubleMap  object out of it.
        """
        sizes = [256, 512, 1024]
        if codeSize not in sizes:
            raise Exception("Code sizes other than 256, 512, 1024 are not supported")
        codeFilenameWithPath = f"digrCodes/digrCode{codeSize}.txt"
        codeArray = self.read_code(codeFilenameWithPath)
        if not codeArray:
            raise Exception(f"{codeFilenameWithPath} not found. Use 'digrcode.py' to construct code.")
        self.cdm = CodeDoubleMap(codeArray)

    def compressAndWrite(self, filename : str, path : str):
        """
        @param
        filename -> ONLY filename, no path
        path -> path to file

        Calls digr_encoder() to compress a file and write it to a binary file
        """

        fileToCompress = open(f'{path}{filename}', "r")
        text = fileToCompress.read()
        # main call
        encodedBits = self.digr_encoder(text, self.cdm)
        
        if not os.path.exists('encodings'):
            os.makedirs('encodings')
            print("Created directory './encodings/'")
        binFileName = f'encodings/{filename}.digr'
        with open(binFileName, 'wb') as binaryFile:
            encodedBits.tofile(binaryFile)
        print(f"Compressed file written to {binFileName}")

    def decompressAndWrite(self, filename: str, path: str):
        """
        @param
        filename -> ONLY filename, no path
        path -> path to file

        Calls digr_encoder() to decompress a binary file and write it to a text file
        """
        compressedFile = open(f'{path}{filename}.digr', "rb")
        bitString = bs.Bits(compressedFile)
        # main call
        decodedText = self.digr_decoder(bitString , self.cdm)

        if not os.path.exists('decodings'):
            os.makedirs('decodings')
            print("Created directory './decodings/'")
        decompressedFilename = f'decodings/{filename}'
        with open(decompressedFilename, 'w') as decompressedFile:
            decompressedFile.write(decodedText)
        print(f"Decompressed file written to {decompressedFilename}")

    def digr_encoder(self, text : str, cdm : CodeDoubleMap) -> bs.BitArray:
        """
        @param
        text -> String we want to encode
        cdm -> the code we are using to encode

        @return
        encodedMsg -> compressed bitstring (in BitArray format)

        Uses digram encoding to compress a text file

        Algorithm:
        Read text file a digram at a time. 
        If digram is in our code, add the appopriate codeword to the encodedMsg. Continue to read the next digram
        If it isn't, add the codeword for the unigram at the current index to encodedMsg. Continue to read digram after the aforementioned unigram.
        """
        encodedMsg = bs.BitArray()
        i = 0

        while i < len(text):
            if i == len(text) - 1: # no digram left to read
                digramCodeword = None 
            else:
                input = text[i:i+2]
                digramCodeword = cdm.getIntCodeword(input)
            if digramCodeword: # if the digram is in our code, encode digram
                encodedMsg += "0b" + dc.getBin(digramCodeword, cdm.codewordLen)
                i += 2
            else: # if the digram is not in our code, encode the unigram
                input = text[i]
                unigramCodeword = cdm.getIntCodeword(input)
                if unigramCodeword: # only encode if it's a printable unigram
                    encodedMsg += "0b" + dc.getBin(unigramCodeword, cdm.codewordLen)
                i += 1
        assert len(encodedMsg) % cdm.codewordLen == 0, "length of encoded message should be k * codewordLen long"
        return encodedMsg

    def digr_decoder(self, bitStr: bs.Bits, cdm : CodeDoubleMap) -> str:
        """
        Since all code words are the same length, simply read cdm.codeWordLen number of bits at a time
        @param:
        bitStr: bs.Bits -> bit string
        cdm -> CodeDoubleMap

        @return
        decodedMsg : str -> String of decoded text
        """
        decodedMsg = []
        for i in range(0, len(bitStr), cdm.codewordLen):
            intCodeword = bitStr[i:i + cdm.codewordLen].int
            decodedMsg.append(cdm.getSymbol(intCodeword))
        return ''.join(decodedMsg)
    
    def read_code(self, filenameWithPath):
        """
        @param
        filenameWithPath : list -> must end with '.digr'
        @return
        codeArray : list -> if codeFile is found
        None ->  otherwise

        Reads a digrCodefile, constructs a codeArray out of it.
        Note that we only need the symbols, as the codewords are
        ordered.
        """
        try:
            codeArray = []
            f = open(filenameWithPath, 'r')
            for line in f:
                symbolAndNewline = line.split('\t')[1]
                symbol = symbolAndNewline[0:len(symbolAndNewline)-1]
                codeArray.append(symbol)
            return codeArray
        except FileNotFoundError:
            return None
    