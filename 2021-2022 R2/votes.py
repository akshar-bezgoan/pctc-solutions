n = int(input())
#name:score
votes = {}
for i in range(n):
    raw = input()
    raw = raw.split()
    raw[0] = raw[0].split(':')
    name = raw[0][0]
    v = raw[0][1]
    n2 = raw[1]
    if name not in votes:
        votes[name] = 0
    
    if n2 in votes:
        if v == 'DOWN':
            votes[n2] -= 1
        else:
            votes[n2] += 1
    else:
        if v == 'DOWN':
            votes[n2] = -1
        else:
            votes[n2] = 1


worst_score = min(votes.values())
people = sorted([person for person, score in votes.items() if score == worst_score])

for i in people:
    print(i)
