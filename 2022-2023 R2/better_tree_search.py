#3147205689

nums = [int(i) for i in input()]
tree = [-1]*1024
tree[0] = int(nums[0])
nums = nums[1:]
def place(num):
    placed = False
    pos = 0
    while not placed:
        if tree[pos] == -1:
            tree[pos] = num
            break
        elif num > tree[pos]:
            pos = 2*pos + 2
        else:
            pos = 2*pos + 1

    return tree

def find_row(row):
    x = 0
    row_curr = [x]
    for i in range(row-1):
        temp = []
        for j in row_curr:
            if tree[(2*j)+1] != -1:
                temp.append((2*j)+1) 
            if tree[(2*j)+2] != -1:
                temp.append((2*j)+2)
        row_curr = temp

    return row_curr
while nums:
    curr = nums.pop(0)
    tree = place(curr)


idx = find_row(int(input()))
for i in idx:
    print(tree[i], end=' ')
    