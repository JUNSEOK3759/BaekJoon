a = int(input())
b = str(input())
b1 = list(map(int, b))
b = int(b)

for i in reversed(range(0, len(b1))):
    print(a * b1[i])

print(a * b)