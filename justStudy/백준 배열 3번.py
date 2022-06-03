x = []
a = range(3)
d = 1
for i in a:
    x.append(int(input(" ")))
d = int(x[0]) * int(x[1]) * int(x[2]) 
y = str(d)
c = range(0, 10)
for j in c:
    print(y.count(str(j)))