lights = int(input())
conn = int(input())
chains, chainPtrs = [], {}

def doAdd(a,b): 
    if a in chainPtrs and b not in chainPtrs:
        chainPtrs[a].add(b)
        chainPtrs[b] = chainPtrs[a]
    elif b in chainPtrs and a not in chainPtrs:
        chainPtrs[b].add(a)
        chainPtrs[a] = chainPtrs[b]
    elif a not in chainPtrs and b not in chainPtrs:
        s = {a,b}
        chains.append(s)
        chainPtrs[a] = s
        chainPtrs[b] = s
    else:
        newS = chainPtrs[b].union(chainPtrs[a])
        chains.remove(chainPtrs[a])
        chains.remove(chainPtrs[b])
        chains.append(newS)
        for x in chainPtrs[a].union(chainPtrs[b]):
          chainPtrs[x] = newS     
    
    print(chainPtrs)
    print(chains)
for _ in range(conn):
    nextConn = input().split(" ")
    doAdd(*nextConn)

print(max(len(l) for l in chains))