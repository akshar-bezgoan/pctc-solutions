ends = {
    0:[0,1,2,3,4,5,6,7,8,9],
    1:[0,1],
    2:[0,5],
    3:[0,7],
    4:[0,5],
    5:[0,2,4,6,8],
    6:[0,5],
    7:[0,3],
    8:[0,5],
    9:[0,9]
}

n = int(input())
m = 1
test = n*m
n_end = ends[int(str(n)[-1])]
def check(num):
    backup = [i for i in str(num) if i == '0' or i == '1']
    if len(backup) == len(str(num)):
        return True
    

while True:
    if int(str(m)[-1]) in n_end:
        test = n*m
        state = check(test)
        if state == True:
            break
    m += 1


print(test)