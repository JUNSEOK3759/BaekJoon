a = int(input())

b = list(map(int, input().split()))

m = max(b)
sum = 0
for i in range(a):
    b[i] = b[i] / m * 100
    sum += b[i]
print(sum / a)