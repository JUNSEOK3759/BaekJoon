hour, min = map(int, input().split())
time = int(input())

time_h = time // 60
time_m = time % 60

hour += time_h
min += time_m

if min >= 60:
    hour += 1
    min -= 60

if hour >= 24:
    hour -= 24


print(hour, min)