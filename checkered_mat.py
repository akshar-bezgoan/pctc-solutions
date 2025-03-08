w = int(input())
h = int(input())
recurr = 0
sym = ['@@@', '###']
for x in range(h):
    for i in range(3):
        curr = recurr
        for j in range(w):
            print(sym[curr], end='')
            curr += 1
            if curr > 1:
                curr = 0
        print('\n', end='')
    recurr += 1
    if recurr > 1:
        recurr = 0
