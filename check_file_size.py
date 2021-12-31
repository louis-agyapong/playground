import os
import sys

path = "docs/example.txt"

try:
    size = os.path.getsize(path)
except OSError:
    print("File Error")
    sys.exit()

print(f"File size: {size} bytes")

print(os.stat(path).st_size)
