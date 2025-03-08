stones = int(input())
players = int(input())
counting_num = int(input())
rounds = int(input())
move_num = players - 1
turn = 'r'
board = ['r' for i in range(players)] + ['_'] + ['b' for i in range(players)]
for i in range(rounds):
  if turn == 'r':
    if board[move_num+1] == '_':
      board[move_num+1],board[move_num] = board[move_num], board[move_num+1]
    elif board[move_num+2] == '_':
      board[move_num+2],board[move_num] = board[move_num], board[move_num+2]
    turn = 'b'
    print(''.join(board))
  if turn == 'b':
    if board[-1*(move_num+1)-1] == '_':
      board[-1*(move_num+1)-1], board[-1*(move_num+1)] = board[-1*(move_num+1)], board[-1*(move_num+1)-1]
    elif board[-1*(move_num+1)-2] == '_':
      board[-1*(move_num+1)-2], board[-1*(move_num+1)] = board[-1*(move_num+1)], board[-1*(move_num+1)-2]
    turn = 'r'
    print(''.join(board))
  if move_num + counting_num + 1 > 3:
    move_num = 0
  else: 
    move_num += counting_num
  