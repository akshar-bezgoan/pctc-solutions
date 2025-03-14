from collections import defaultdict

n = int(input())
cons = int(input())
rels = defaultdict(list)

for i in range(cons):
    n1, n2 = input().split(' ')
    rels[n1].append(n2)

def get_length(n):
    if n not in rels:
        return 1
    elif len(rels[n]) == 1:
        return get_length(rels[n][0]) + 1
    else:
        return get_length(rels[n][0]) + get_length(rels[n][1]) + 1
    
def find_max():
    max = 0
    for j in rels:
        temp = get_length(j)
        if temp > max:
            max = temp

if cons != 0:
    print(find_max())
else: 
    print(1)

    