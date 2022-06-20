import sys

a = int(input())

for i in range(a):
    h, w, n = map(int, sys.stdin.readline().split())
    floor = n % h
    room = n // h + 1
    if n % h == 0:
        floor = n
        room = n // h
    print(f'{floor * 100 + room}')