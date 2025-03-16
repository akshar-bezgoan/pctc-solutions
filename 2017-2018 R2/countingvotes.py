votes = int(input())
y, n = 0,0
for i in range(votes):
    vote = input()
    if vote == 'YES':
        y +=1
    elif vote == 'NO':
        n += 1

print(f'YES {y}')
print(f'NO {n}')