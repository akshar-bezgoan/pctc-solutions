error = False
while not error:
    w1, w2 = input().split()
    if w1 != w2:
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                print(w1[i], w2[i])
                error = True
                break
        if error == False:
            if len(w1) > len(w2):
                print(w1[-1], '_')
            else:
                print('_', w2[-1])
            error = True
            break


    