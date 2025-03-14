import math
d = 779721000 #m
s = int(input()) #m/s
t = d/s #in seconds
t /= 3600
print(math.ceil(t))