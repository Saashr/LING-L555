import sys

s = sys.stdin.readline()
while s:
    print(s.replace('. ','.\n').replace('۔','۔\n'))
    s = sys.stdin.readline()

