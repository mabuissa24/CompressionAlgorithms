import bitstring as bs
import digrCode as dc
import os

TEXT = "The United States had a thriving space station consisting of two main structures; the North Tower and the South Tower, each filled with Crewmates going about their daily tasks. However, a group of Impostors disguised as Crewmates, had infiltrated the station and were plotting to cause chaos. On one fateful day, the Impostors hijacked two spacecrafts and piloted them towards the two towers. The Crewmates on the ground watched in horror as the spacecrafts crashed into the towers, causing massive explosions and fires. The Crewmates in the towers scrambled to evacuate, but many were trapped as the buildings began to collapse. Emergency Crewmates, including firefighters and medical personnel, rushed to the scene to help their colleagues and put out the fires and complete tasks. Among U.S catastrophes, this was the most devastating in history, with thousands of innocent Crewmates losing their lives. The United States vowed to find those responsible for the attack, and to eject them. They issued an emergency meeting and began to track down the Impostors who had carried out the horrific act of violence."

class CodeDoubleMap:
    def __init__(self, codeArray: list):
        self.reverseMap = {}
        self.codeArray = codeArray
        self.codewordLen = dc.bitsRequired(len(codeArray) - 1)
        for i in range(len(codeArray)):
            self.reverseMap[codeArray[i]] = i

    def getSymbol(self, codeWord: int):
        return self.codeArray[codeWord]

    def getIntCodeword(self, symbol):
        try:
            codeWord = self.reverseMap[symbol]
            return codeWord
        except KeyError:
            return None


class DigramCompression:
    def __init__(self, codeSize: int):
        sizes = [256, 512, 1024]
        if codeSize not in sizes:
            raise Exception("Code sizes other than 256, 512, 1024 are not supported")
        code = self.read_code(f"digrCode{codeSize}.txt")
        self.cdm = CodeDoubleMap(code)

    def compressAndWrite(self, filename : str):
        fileToCompress = open(filename, "r")
        text = fileToCompress.read()
        encodedBits = self.digr_encoder(text, self.cdm)
        
        if not os.path.exists('encodings'):
            os.makedirs('encodings')
        with open(f'encodings/{filename}.digr', 'wb') as binaryFile:
            encodedBits.tofile(binaryFile)

    def decompressAndWrite(self, filename: str):
        compressedFile = open(f'{filename}.digr', "rb")
        bitString = bs.Bits(compressedFile)
        decodedText = self.digr_decoder(bitString)

        if not os.path.exists('decodings'):
            os.makedirs('decodings')
        with open(f'decodings/{filename}.txt', 'w') as decompressedFile:
            decompressedFile.write(decodedText)

    def digr_encoder(self, text : str, cdm : CodeDoubleMap) -> bs.BitArray:
        encodedMsg = bs.BitArray()
        i = 0
        while i < len(text):
            if i == len(text) - 1: # no digram left to read
                digramCodeword = None 
            else:
                input = text[i:i+2]
                digramCodeword = cdm.getIntCodeword(input)
            if digramCodeword: # encode digram
                encodedMsg += "0b" + dc.getBin(digramCodeword, cdm.codewordLen)
                i += 2
            else: # encode unigram
                input = text[i]
                unigramCodeword = cdm.getIntCodeword(input)
                if unigramCodeword: # only encode if it's a printable unigram
                    encodedMsg += "0b" + dc.getBin(unigramCodeword, cdm.codewordLen)
                i += 1
        assert len(encodedMsg) % cdm.codewordLen == 0, "length of encoded message should be k * codewordLen long"
        return encodedMsg

    def digr_decoder(self, bitStr: bs.Bits, cdm : CodeDoubleMap) -> str:
        decodedMsg = []
        for i in range(0, len(bitStr), cdm.codewordLen):
            decodedMsg.append(cdm.getSymbol(bitStr[i:i + cdm.codewordLen].int))
        return ''.join(decodedMsg)
    
    def read_code(self, filename):
        """
        Reads a file, constructs a codeArray out of it.
        Note that we only need the symbols, as the codewords are
        ordered.
        """
        codeArray = []
        f = open(filename, 'r')
        for line in f:
            symbolAndNewline = line.split('\t')[1]
            symbol = symbolAndNewline[0:len(symbolAndNewline)-1]
            codeArray.append(symbol)
        return codeArray
    