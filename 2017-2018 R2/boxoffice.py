r,s = map(int, input().split())
theatre = []
for i in range(r):
    theatre.append(['0']*s)

def findSeats(row, size, theatre):
    l = 0
    h = l+size
    while h < s+1:
        if ''.join(theatre[row][l:h]) == '0'*size:
            for i in range(l,h):
                theatre[row][i] = '1'
            return theatre
        l+= 1
        h+=1
    return theatre


n = int(input())
for i in range(n):
    size = int(input())
    for j in range(len(theatre)):
        if ''.join(theatre[j]).count('0'*size) >= 1:
            row = j
            theatre = findSeats(row, size, theatre)
            break
    
tickets = 0
for i in theatre:
    tickets += ''.join(i).count('1')

print(tickets)