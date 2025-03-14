from collections import defaultdict
n = int(input())
def x(n):
    cons = int(input())
    if cons == 0:
        return 1

    lights = defaultdict(set)

    for i in range(cons):
        n1, n2 = input().split()
        n1, n2 = int(n1), int(n2)
        lights[n1].add(n2)
        lights[n2].add(n1)
        
    new = defaultdict(set)
    print(lights)

    for i in lights:
        for j in lights[i]:
            if not new[j]:
                new[i] |= lights[j]
            else:
                new[i] |= new[j]
            new[i] |= lights[i]

    print(new)

    maxx = 0
    for i in new:
        if len(new[i]) > maxx:
            maxx = len(new[i])


    return maxx


if n == 1 or n == 0:
    print(n)
else:
    print(x(n))