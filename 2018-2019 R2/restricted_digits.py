from math import factorial
from collections import defaultdict

num = int(input())
counter = defaultdict(int)
for i in str(num):
    counter[int(i)] += 1

dupes = 1
for m in counter:
    dupes *= factorial(counter[m])

n = len(str(num))
sum = 0
for j in counter:
    for k in range(0,n):
        appearances = counter[j]
        col_num = (appearances * factorial(n-1)) // dupes
        sum += (col_num * j * (10**k))

print(sum)

