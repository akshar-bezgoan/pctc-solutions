p = int(input())
t = int(input())
x = int(input())
y = int(input())

total = 0
for i in range(t):
    interest = (p//x)*y
    p += interest
    total += interest

print(f'${total}')