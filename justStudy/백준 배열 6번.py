a = int(input())
for i in range(a):
    b = list(map(int, (input(). split(" "))))
    avg = sum(b[1:]) / b[0]
    count = 0
    for j in b[1:]:
        if j > avg:
            count += 1
    print ("%.3f%%" % round(count / b[0] * 100,3))