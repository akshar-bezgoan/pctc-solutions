ls = [i for i in input()]
lst = []
for i in ls:
    if i != ',':
        lst.append(i)

lastest = 0
ans = []
i = 0
while len(lst) != 0:
    if i < len(lst):        
        if lst[i] == '[':
            latest1 = i
        elif lst[i-1] == '[':
            n1 = lst[i]
        i += 1
        if lst[i] == ']':
            n2 = lst[i-1]
            mean = (int(n1) + int(n2))//2
            ans.append(mean)
            del lst[latest1:i+1]
            i = 0
    else:
        i = 0

ans = [str(i) for i in ans]
print(''.join(ans))
    


#[4,[2,8],[5,9,[3]],6]
#['[', '4', '[', '2', '8', ']', '[', '5', '9', '[', '3', ']', ']', '6', ']']