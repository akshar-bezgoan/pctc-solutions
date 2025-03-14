person = ['', 0]
for i in range(3):
    p = input().split()
    name = p[0]
    age = int(p[1])
    if age > person[1]:
        person = [name, age]

w1 = max(4, len(person[0]))

print(f'|{"NAME":<{w1}}|AGE|')
print(f'|{"-" * w1}|---|')
print(f'|{person[0]:<{w1}}|{person[1]:<3}|')