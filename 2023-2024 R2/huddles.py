n = int(input())
coords = []
for i in range(n):
	coords.append([int(i) for i in input().split(',')])

moved = True
while moved:
	moved = False
	demand = {}
	for i in range(n):
		if coords[i][0] > 0:
			x = coords[i][0] - 1
		elif coords[i][0] < 0:
			x = coords[i][0] + 1
		else:
			x = coords[i][0]
		if coords[i][1] > 0:
			y = coords[i][1] - 1
		elif coords[i][1] < 0:
			y = coords[i][1] + 1
		else:
			y = coords[i][1]
		mv = (x,y)
		if list(mv) in coords:
			continue
		elif mv in demand.keys():
			demand[mv].append(coords[i])
		else:
			demand[mv] = [coords[i]]
			
	for j in demand.keys():
		if len(demand[j]) == 1:
			coords[coords.index(demand[j][0])] = list(j)
			moved = True

score = 0
for i in coords:
	score += abs(i[0]) + abs(i[1])

print(score)
		



'''
[[1, 2], [4, 2], [4, -1], [-3, 6], [-2, 5], [0, 1], [-4, -3], [-2, -5]]


{(0, 1): [[1, 2]], 
(3, 1): [[4, 2]], 
(3, 0): [[4, -1]], 
(-2, 5): [[-3, 6]], 
(-1, 4): [[-2, 5]], 
(0, 0): [[0, 1]], 
(-3, -2): [[-4, -3]], 
(-1, -4): [[-2, -5]]}


[(0, 1), (3, 1), (3, 0), (-2, 5), (-1, 4), (0, 0), (-3, -2), (-1, -4)]
[[1, 2], [4, 2], [4, -1], [-3, 6], [-2, 5], [0, 1], [-4, -3], [-2, -5]]


'''
