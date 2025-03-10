n = int(input())
m = int(input())
s1 = input()
s2 = input()
gap = (n-m-2)//2
print(s1*n)
for i in range(gap):
    print(s1+' '*(n-2)+s1)
for i in range(m):
    print(s1+' '*(gap)+s2*m+' '*(gap)+s1)
for i in range(gap):
    print(s1+' '*(n-2)+s1)
print(s1*n)
