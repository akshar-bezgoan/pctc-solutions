map = [
    [0,'A',0,0,0,0],
    [0,'A','D','D','D','D'],
    [0,'A',0,0,0,0],
    [0,'A',0,0,0,'S'],
    [0,'A',0,0,0,'S'],
    ['P','P',0,0,0,'S'],
    ]

og = [5,4,3,2]
counts = [5,4,3,2]
def conv(coord):
    coord = coord.split()
    coord[0], coord[1] = int(coord[1]), int(coord[0])
    coord[0] -= 1
    coord[1] -= 1
    return coord

def chc(shot, map, counts=og):

    loc = map[shot[0]][shot[1]]
    if loc == 'A':
        counts[0] -= 1
    elif loc == 'D':
        counts[1] -= 1
    elif loc == 'S':
        counts[2] -= 1
    elif loc == 'P':
        counts[3] -= 1
    map[shot[0]][shot[1]] = 0
    return counts

shots = int(input())
for i in range(shots):
    shot = conv(input())
    counts = chc(shot, map, counts)

uh = 0
hba = 0
hs = 0
for i in range(len(counts)):
    if counts[i] == 0:
        hs += 1
    elif counts[i] == og[i]:
        uh += 1
    else:
        hba += 1

print(f'UNHARMED:{uh}')
print(f'HIT BUT AFLOAT:{hba}')
print(f'HIT AND SUNK:{hs}')