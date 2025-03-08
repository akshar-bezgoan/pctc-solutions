def marathon(n):
    p = []
    for i in range(n):
        p.append(input().split())
    for i in range(len(p)):
        time = p[i][1]
        time = time.split(':')
        time[-1] = time[-1].split('.')
        nt = [int(time[i]) for i in range(2)]
        nt.append(int(time[-1][0]))
        nt.append(int(time[-1][1]))
        total = nt[0] * 60 * 60 + nt[1] * 60 + nt[2] + nt[3] * 24 * 60 * 60
        p[i][1] = total
    print(p)

marathon(4)
