a = input()
a = a.lower()
max = 0
s1 = set(a)
ans = []

for i in s1:
    c = a.count(i)
    if max < c:
        max = c
        ans = []
        ans.append(i.upper())
    elif max == c:
        ans = '?'
print(ans[0])