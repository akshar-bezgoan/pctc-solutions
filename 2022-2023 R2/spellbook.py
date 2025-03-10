n = int(input())
book = [0] * (n + 1)
for i in range(1, n + 1):
    book[i] = int(input())


cache = [-1] * (n + 1)

def find_spell_length(start):
    if cache[start] != -1: 
        return cache[start]

    visited = {}
    curr = start
    steps = 0

    while curr not in visited:
        if cache[curr] != -1:  
            spell_length = steps + cache[curr]
            for page in visited:
                cache[page] = spell_length - visited[page]
            return cache[start]
        
        visited[curr] = steps
        steps += 1
        curr = book[curr]
    cycle_length = steps - visited[curr]
    
    for page, step in visited.items():
        if step >= visited[curr]:
            cache[page] = cycle_length
        else:
            cache[page] = cycle_length + (visited[curr] - step)

    return cache[start]

max_length = 0
freq = 0

for i in range(1, n + 1):
    spell_length = find_spell_length(i)
    if spell_length > max_length:
        max_length = spell_length
        freq = 1
    elif spell_length == max_length:
        freq += 1

print(max_length)
print(freq)
