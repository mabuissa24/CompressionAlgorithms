from digrXXX import DigramCompression
import sys

if __name__ == "__main__":
    if len (sys.argv) != 2:
        print("Usage: python digr256C.py <filepath>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    dc = DigramCompression(256)
    dc.compressAndWrite(filepath)