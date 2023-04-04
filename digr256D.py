from digrXXX import DigramCompression
import sys

if __name__ == "__main__":
    if len (sys.argv) != 2:
        print("Usage: python digr256D.py <filepathNoExtension>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    if ".digr" in filepath:
        print("Usage: python digr256D.py <filepathNoExtension>")
        print("Do not include code extension '.digr'")
        sys.exit(1)
    dc = DigramCompression(256)
    dc.decompressAndWrite(filepath)