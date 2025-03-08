num = int(input())
al = [num]
while num != 0:
    nums = [int(i) for i in str(num)]
    total = 0
    for i in nums:
        total += i
    num -= total
    total = 0
    al.append(num)	
print(len(al))

