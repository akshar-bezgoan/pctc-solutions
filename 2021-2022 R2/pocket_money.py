n1,n2 = sorted([int(input()), int(input())])
if n1 < 10:
    np1 = f'0{n1}'
else:
    np1 = n1
if n2 < 10:
    np2 = f'0{n2}'
else:
    np2 = n2
if n2 < 20 or n2 ==20 and n1 == 0:
    print(f'£{n1}.{np2}')
    print(f'£{n2}.{np1}')
else:
    print(f'£{n1}.{np2}')