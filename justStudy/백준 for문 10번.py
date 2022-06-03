n = input("")
a = range(1,int(n)+1, 1)
for i in a:
    b = "*" * i
    print(b.rjust(int(n)))