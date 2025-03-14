s = input()
new = input()
count = 0
for i in new:
    if i not in s:
        count += 1
        s += i
print(count)