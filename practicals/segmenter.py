import sys

try:
    s = sys.stdin.readline()
    while s:
        print(s.replace('۔', '۔\n'))
        s = sys.stdin.readline()
except BrokenPipeError:
    pass  # Handle or log as necessary

