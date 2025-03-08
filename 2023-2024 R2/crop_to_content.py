n = int(input())
arr= []
for i in range(n):
	arr.append([i for i in input()])

top = []
for i in range(len(arr)):
	for j in range(len(arr)):
		if arr[i][j] != '.':
			top.append(i)
			break
bounds = [top[0]-1, top[-1]+1]


uncut = arr
top, bottom = bounds[0], bounds[1]
new_arr = [uncut[i] for i in range(top+1, bottom)] 

left = []
for i in range(len(arr[0])):
	for j in range(len(arr)):
		if arr[j][i] != '.':
			left.append(i)
			break
cbounds = [left[0], left[-1]]

new = []
for i in range(len(new_arr)):
	temp = []
	for j in range(cbounds[0], cbounds[1] + 1):
		temp.append(new_arr[i][j])
	new.append(temp)

for i in range(len(new)):
	print(''.join(new[i]))



'''
[0['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 1['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 2['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
 3['.', '.', '~', '~', '.', '{', '@', '%', '%', '@', '}', '.', '.', '~', '.', '.', '.'], 
 4['.', '.', '~', '~', '.', '{', '@', '%', '%', '@', '}', '.', '.', '~', '.', '.', '.'], 
 5['.', '.', '~', '~', '.', '{', '@', 'X', 'X', '@', '}', '.', '.', '~', '.', '.', '.'], 
 6['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
 7['.', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '.'], 
 8['.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.'], 
 9['.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.'], 
 10['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
 11['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
 12['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
 13['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
 14['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
 15['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
 16['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]


   0    1    2
0['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
1['.', '.', '~', '~', '.', '{', '@', '%', '%', '@', '}', '.', '.', '~', '.', '.', '.'], 
2['.', '.', '~', '~', '.', '{', '@', '%', '%', '@', '}', '.', '.', '~', '.', '.', '.'], 
3['.', '.', '~', '~', '.', '{', '@', 'X', 'X', '@', '}', '.', '.', '~', '.', '.', '.'], 
4['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
5['.', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '.'], 
6['.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.'], 
7['.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.'], 
8['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']



[['~', '~', '.', '{', '@', '%', '%', '@', '}', '.', '.', '~'], 
['~', '~', '.', '{', '@', '%', '%', '@', '}', '.', '.', '~'], 
['~', '~', '.', '{', '@', 'X', 'X', '@', '}', '.', '.', '~'], 
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#'], 
['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#']]

'''

