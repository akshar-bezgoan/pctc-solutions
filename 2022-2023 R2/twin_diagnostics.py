p1, age1 = input().split()
p2, age2 = input().split()

age1 = int(age1)
age2 = int(age2)


if age1 == age2: 
  print(f"MAYBE TWINS:{p1} and {p2} are the same age")
elif age1 > age2:
  print(f"NOT TWINS:{p1} is {age1 - age2} year(s) older than {p2}")
else:
  print(f"NOT TWINS:{p1} is {age2 - age1} year(s) younger than {p2}")