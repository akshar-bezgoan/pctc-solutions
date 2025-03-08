score = [0,0]
recent = -1

for i in range(6):
    plays = [i for i in input()]
    if 'W' not in plays:
        if plays[0] == "R":
            if plays[1] == "P":
                score[1]+=1
            elif plays[1] == "S":
                score[0]+=1
        elif plays[0] == "P":
            if plays[1] == "S":
                score[1]+=1
            elif plays[1] == "R":
                score[0]+=1
        else:
            if plays[1] == "R":
                score[1]+=1
            elif plays[1] == "P":
                score[0]+=1

    else:
        if plays[1] == 'W' and plays[0] != 'W':
            score[1] += 1
            recent = 1
        elif plays[1] != 'W' and plays[0] == 'W':
            score[0] += 1
            recent = 0
        elif recent != -1:
            score[recent] = 0

print(f'{score[0]}-{score[1]}')