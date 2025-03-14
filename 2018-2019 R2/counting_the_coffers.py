def cOrD(state, money):
    if state == 'CR':
        return money
    else:
        return money * -1
cd, balance = input().split()
balance = int(balance)
balance = cOrD(cd, balance)

n = int(input())
for i in range(n):
    temp = input().split()
    mon = int(temp[1])
    balance += cOrD(temp[0], mon)

if balance < 0:
    print(f'DR {-1 *balance}')
else:
    print(f'CR {balance}')