x = []
a = range(10)
s = []
for i in a:
    x.append(int(input("")))
    s.append(x[i] % 42)
print(len(set(s)))