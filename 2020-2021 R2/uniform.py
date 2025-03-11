d = int(input())
s = input()
if s == 'TUCKED' or s == 'UNTUCKED':
    shirt = s
    tie = input()
else:
    tie = s
    shirt = input()

if tie == 'LOOSE':
    d += 5
elif shirt == 'UNTUCKED':
    pass
else:
    d = 0
print(d)