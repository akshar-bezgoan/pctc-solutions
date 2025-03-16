n1, n2, n3 = sorted([int(input()), int(input()), int(input())])
if n1 + n2 == n3 or n1 + n3 == n2:
    print('HAPPY CROWD')
else:
    print('UNHAPPY CROWD')