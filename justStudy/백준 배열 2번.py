x = []
a = range(9)
for i in a:
    x.append(int(input("")))
print(max(x))
print(x.index(max(x))+1)