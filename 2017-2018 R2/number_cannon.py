n = int(input())
def add(l, a):
    d = l-a+1
    return ((a+l)*d)//2

x = add(n, 1)
y = add(x, 1)
print(y)