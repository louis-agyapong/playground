import os
import sys

path = "docs/xample.txt"

try:
    size = os.path.getsize(path)
except OSError:
    print("File Error")
    sys.exit()

print(f"File size: {size} bytes")
