num = temp = int(input())
count = 0
while True:
    a = num / 10
    b = num % 10 
    c = a + b 
    count += 1
    num = int(str(num % 10) + str(c % 10))
    if temp == num:
        break
print(count)
