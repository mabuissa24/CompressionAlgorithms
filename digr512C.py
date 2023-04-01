from digrXXX import DigramCompression
import sys

if __name__ == "__main__":
    if len (sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: python digr256C.py <filename> [pathToFile]")
        print("Default path: './'")
        print("Example pathToFile: './books/")
        sys.exit(1)
    
    filenameWithPath = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) == 3 else "./"
    dc = DigramCompression(512)
    dc.compressAndWrite(filenameWithPath, path)