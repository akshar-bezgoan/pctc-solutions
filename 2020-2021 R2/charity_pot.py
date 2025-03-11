import math

n = int(input())
p = int(input())
paid = math.ceil(p/n) * n
charity = paid - p
print(charity)