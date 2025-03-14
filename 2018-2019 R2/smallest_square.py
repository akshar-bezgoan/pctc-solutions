import math
#9/10 Testcases passed:
n = input()
found = False
dta = 1 #digits to append
while not found:
    for i in range(10**(dta-1),10**dta):
        trial = int(str(i)+str(n))
        if math.ceil(math.sqrt(trial)) == math.floor(math.sqrt(trial)):
            print(int(trial))
            found = True
            break

    dta += 1

#10/10 Testcases passed

ending = input()
digits = len(ending)
x = 1
while True:
    if str(x**2)[-digits:] == ending:
        print(x**2)
        break
    x += 1


