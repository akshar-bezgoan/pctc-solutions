p,t,w = map(int, input().split())

def round(curr, players, t, w):
    next = curr + t
    curr = curr%len(players)
    del players[curr]
    w -= 1
    return curr, w

players = [i for i in range(1,p+1)]
curr = t

while w > 0 and len(players) != 1:
    curr, w = round(curr, players, t, w)
    

curr %= p
curr = chr(curr+65)
print(curr)