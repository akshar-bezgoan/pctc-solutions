s_count = 0
h = 0
bloom = False
for i in range(7):
    day = input()
    if day[1] == 'r':
        h += 1
    if day[0] == 's':
        s_count += 1
    elif day[0] == 'c':
        s_count = 0
    if s_count == 3:
        bloom = True

if bloom == True:
    print('***')
for i in range(h):
    print(" | ")
print("\_/")