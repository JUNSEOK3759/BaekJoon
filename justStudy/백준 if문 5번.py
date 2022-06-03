a, b = map(int, input("").split(" "))
if  0 <= a <= 23:
    if 0 <= b <= 59: 
        if b > 45:
            print(a, b -45)
        elif b == 45:
            print(a, 0)
        else:
            if a == 0:
               print(23, 60 - (45 - b))
            else:
                print(a -1 , 60 - (45 - b))