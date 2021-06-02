n = int(input(""))
a = list(map(float, input().split(" ")))
b = []
sum = 0
for i in range(n):
    b.append(a[i] / max(a) * 100)
    sum += b[i]
print(sum / n)
