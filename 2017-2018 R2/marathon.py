from collections import defaultdict
n = int(input())
times = defaultdict(int)

def convert(time):
    h,m,s,d = time
    h*= 3600
    m *= 60
    
    return float(h+m+s) + d/10

for i in range(n):
    raw = input().replace('.', ':').split()
    times[raw[0]] = convert(list(map(int, raw[1].split(':'))))


final = []
for i in times:
    if times[i] <= times['Percy']:
        final.append(i)

print(len(final))