#3/10 testcases - not the right solution!

x, y = map(list, input().split())
centre = []
won = False
turn = 1
pay = {'A':4, 'K':3, 'Q':2, 'J':1}

def move(x,y,centre,turn):
    won = False
    if turn == 1:
        centre.append(x.pop(0))
    elif turn == -1:
        centre.append(y.pop(0))
    if centre[-1] in pay.keys():
        x,y,centre,turn, won = get_debt(x,y,centre,turn*-1)

    return x,y,centre,turn*-1, won

def get_debt(x,y,centre, turn):
    amount = pay[centre[-1]]
    for i in range(amount):
        x,y,centre,turn,won = move(x,y,centre,turn)
        if won == True:
            return x,y,centre,turn,won
        turn *= -1

    if turn == 1:
        for i in range(len(centre)):
            y.append(centre[i])
        centre = []
    else:
        for i in range(len(centre)):
            x.append(centre[i])
        centre = []

    won = True
    return x,y,centre,turn*-1, won
rounds = int(input())
for i in range(rounds):
    won = False
    while won == False:
        x,y,centre,turn, won = move(x, y, centre, turn)
print(''.join(x))