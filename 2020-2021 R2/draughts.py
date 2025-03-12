board = [['.', 'b', '.', 'b', '.', 'b', '.', 'b'], 
    ['b', '.', 'b', '.', 'b', '.', 'b', '.'], 
    ['.', 'b', '.', 'b', '.', 'b', '.', 'b'], 
    ['.', '.', '.', '.', '.', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '.', '.', '.'], 
    ['w', '.', 'w', '.', 'w', '.', 'w', '.'], 
    ['.', 'w', '.', 'w', '.', 'w', '.', 'w'], 
    ['w', '.', 'w', '.', 'w', '.', 'w', '.']]

moves = int(input())

def conv(inp, reverse):
    switches = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    lr = {'L': 'R', 'R': 'L'}

    inp[0] = switches[inp[0]]
    inp[1] = 8 - int(inp[1])
    inp[0], inp[1] = inp[1], inp[0]  
    
    if reverse:
        inp[2] = lr[inp[2]]  

    return inp
    
def new(move, player):
    curr = (move[0], move[1]) 

    if player == 'W': 
        new_pos = (curr[0] - 1, curr[1])
    else:  
        new_pos = (curr[0] + 1, curr[1])

    if move[2] == 'L':  
        new_pos = (new_pos[0], new_pos[1] - 1)
    else: 
        new_pos = (new_pos[0], new_pos[1] + 1)

    return list(curr), list(new_pos), move[2]

def update(curr, new, dir, player):
    new_pos_val = board[new[0]][new[1]] 
    old_pos_val = board[curr[0]][curr[1]] 
    
    if new_pos_val == '.':
        board[new[0]][new[1]] = old_pos_val 
        board[curr[0]][curr[1]] = '.'  
    elif player == 'W': 
        if dir == 'L': 
            jump_pos = (new[0] - 1 , new[1] - 1)
        else: 
            jump_pos = (new[0] - 1, new[1] + 1)
    
        board[jump_pos[0]][jump_pos[1]] = old_pos_val 
        board[curr[0]][curr[1]] = '.' 
        board[new[0]][new[1]] = '.'  


    elif player == 'B': 
        if dir == 'L': 
            jump_pos = (new[0] + 1 , new[1] - 1)
        else: 
            jump_pos = (new[0] + 1, new[1] + 1)

        board[jump_pos[0]][jump_pos[1]] = old_pos_val 
        board[curr[0]][curr[1]] = '.' 
        board[new[0]][new[1]] = '.'  

    return board

for i in range(1, moves + 1):
    if i % 2 == 0:
        reverse = True
        player = 'B'
    else:
        reverse = False
        player = 'W'

    curr, new_pos, direction = new(conv([i for i in input()], reverse), player)
    board = update(curr, new_pos, direction, player)

for row in board:
    print(''.join(row))


'''
[['.', 'b', '.', 'b', '.', 'b', '.', 'b'], 
['b', '.', 'b', '.', 'b', '.', 'b', '.'], 
['.', '.', 'b', 'b', '.', 'b', '.', 'b'], 
['.', '.', '.', '.', '.', '.', '.', '.'], 
['.', '.', '.', 'w', '.', '.', '.', '.'], 
['.', '.', 'w', '.', '.', '.', 'w', '.'], 
['w', 'w', '.', 'w', '.', 'w', '.', 'w'], 
['w', '.', 'w', '.', 'w', '.', 'w', '.']]
'''


'''
4
a3R
b6L
e3L
c5R
'''