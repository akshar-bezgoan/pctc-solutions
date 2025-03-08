x1 = int(input())
y1 = int(input())
z1 = int(input())
s1 = int(input())
x2 = int(input())
y2 = int(input())
z2 = int(input())
s2 = int(input())

c1 = [[x1, y1, z1], [x1 + s1, y1 + s1, z1 + s1]]
c2 = [[x2, y2, z2], [x2 + s2, y2 + s2, z2 + s2]]

cuboid = [[], []]

for i in range(len(c1[0])):
    if c1[0][i] > c2[0][i]:
        cuboid[0].append(c1[0][i])
    else:
        cuboid[0].append(c2[0][i])

for i in range(len(c1[1])):
    if c1[1][i] < c2[1][i]:
        cuboid[1].append(c1[1][i])
    else:
        cuboid[1].append(c2[1][i])

cx = max(0, cuboid[1][0] - cuboid[0][0])
cy = max(0, cuboid[1][1] - cuboid[0][1])
cz = max(0, cuboid[1][2] - cuboid[0][2])

V = cx * cy * cz
print(V)

		
