n = int(input())
#x1, y1, x1+w=x2, y1+h=y2
intersection = [0,0,1000000000,1000000000] #Constraints are 0<=x,y<=1,000,000
for i in range(n):
    rug = [int(i) for i in input().split()]
    rug[2]+= rug[0]
    rug[3] += rug[1]
    if rug[0] > intersection[0]:
        intersection[0] = rug[0]
    if rug[1] > intersection[1]:
        intersection[1] = rug[1]
    if rug[2] < intersection[2]:
        intersection[2] = rug[2]
    if rug[3] < intersection[3]:
        intersection[3] = rug[3]

area = (intersection[3] - intersection[1]) * (intersection[2] - intersection[0])
print(area)