length = int(input())
coins = [i for i in input()]
moves = 0
plus = 0
for i in range(length):
  if coins[i] == 'T':
    if plus == 0:
      moves -= i
      plus += 1
    elif plus == 1:
      moves += i
      plus -= 1

print(moves)
