ages = 'abcdefghijlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
curr = ages.index(input())
if curr != 0:
    new = curr - 1
else:
    new = curr

print(ages[new])