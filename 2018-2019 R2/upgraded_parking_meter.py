coins = [200, 100, 50, 20, 10, 5, 2, 1]
paid = 0
current_coin = 0
while current_coin != -1:
    current_coin = int(input())
    paid += current_coin

paid += 1
change = paid % 60

coins_to_pay = 0
while change > 0:
    for i in coins:
        if i<=change:
            change -= i
            coins_to_pay += 1

print(coins_to_pay)