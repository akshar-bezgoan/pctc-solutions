runup = 0
path = input()
for i in path:
    if i == '+':
        runup += 5
    elif i == '-':
        runup += 1
    elif i == '/':
        break

speed = runup * 3
buses = path.count('#')
req = buses * 4

if speed > req:
    print('\\')
else:
    print('#'*((speed//4)+1))