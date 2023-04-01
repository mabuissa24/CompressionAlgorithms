from digrXXX import DigramCompression
import sys

if __name__ == "__main__":
    if len (sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: python digr256C.py <filenameNoExtension> [pathToFile]")
        print("Default path: './encodings/'")
        sys.exit(1)
    
    filenameWithPath = sys.argv[1]
    if ".digr" in filenameWithPath:
        print("Usage: python digr256C.py <filenameNoExtension> [pathToFile]")
        print("Do not include code extension '.digr' in filename")
        sys.exit(1)
    path = sys.argv[2] if len(sys.argv) == 3 else "./encodings/"
    dc = DigramCompression(1024)
    dc.decompressAndWrite(filenameWithPath, path)