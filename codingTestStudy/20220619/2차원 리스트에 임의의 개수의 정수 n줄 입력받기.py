import sys

data = []

a = int(sys.stdin.readline())

for i in range(a):
    data.append(list(map(int, sys.stdin.readline().split())))
print(data)