import sys
a = int(input())

for i in range(a):
    b, c = map(str, sys.stdin.readline().split())
    b = int(b)
    for j in range(len(c)):
        print(c[j] * b, end = '')
    print()