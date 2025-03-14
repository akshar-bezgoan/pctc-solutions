from math import factorial
from collections import defaultdict

num = input()

counter = defaultdict(int)

for i in num:
    counter[i] += 1

dupes = 1
for j in counter:
    dupes *= factorial(counter[j])

combs = factorial(len(num))
perms = combs/dupes


