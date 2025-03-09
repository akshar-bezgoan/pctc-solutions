#3147205689
import math
digits = [int(i) for i in input()]
head = digits[0]
tree = {head:[-1, -1]}

def insert(num,  head=head):
    curr = head
    while(True):
        if num < curr:
            new = tree[curr][0]
            if new == -1:
                tree[curr][0] = num
                tree[num] = [-1, -1]
                return tree
            else:
                curr = new

        elif num > curr:
            new = tree[curr][1]
            if new == -1:
                tree[curr][1] = num
                tree[num] = [-1, -1]
                return tree
            else:
                curr = new


for i in range(1, len(digits)):
    tree = insert(digits[i])


order = [digits[0]]
rows = [[digits[0]]]
while [i for i in order] != [-1] * len(order):
    curr = order[0]
    if curr == -1:
        children = [-1, -1]
    else:
        children = tree[curr]
    rows.append(children)
    order.append(children[0])
    order.append(children[1])
    del order[0]



new_rows = []
# Level 0: 1 element
new_rows.append(rows[0:1])  # First element
# Level 1: 1 element
new_rows.append(rows[1:2])  # Second element

# For the remaining levels, starting from Level 2, we double the number of elements.
index = 2  # Start from the third element
level_size = 2  # Level 2 starts with 2 elements
while index < len(rows):
    new_rows.append(rows[index:index + level_size])  # Append the elements for the current level
    index += level_size  # Move the starting index to the next part
    level_size *= 2  # Double the number of elements for the next level

desired = int(input())
row = new_rows[desired-1]
row = [item for sublist in row for item in sublist]
print(*[i for i in row if i != -1])








#[[[3]], 
# [[1, 4]], 
# [[0, 2], [-1, 7]], 
# [[-1, -1], [-1, -1], [-1, -1], [5, 8]], 
# [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, 6], [-1, 9]], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]]