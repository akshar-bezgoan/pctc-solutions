a, b, c = int(input()), int(input()), int(input())
if a**2 + b **2 < c**2:
  print(f'{a} squared plus {b} squared is less than {c} squared')
elif a**2 + b**2 > c**2:
  print(f'{a} squared plus {b} squared is greater than {c} squared')
else:
  print(f'{a} squared plus {b} squared is equal to {c} squared')