eaten = []
fruit = input()
while len(eaten) < len(fruit):
    eaten.append(fruit)
    fruit = input()

print(len(eaten))