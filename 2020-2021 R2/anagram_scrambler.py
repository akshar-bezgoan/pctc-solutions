w = input()
n = int(input())

def shift(w, n):
    w = [i for i in w]
    for i in range(n):
        letter = w.pop(0)
        w.append(letter)
    return ''.join(w)

anagram = ''
while len(w) != 0:
    w = shift(w, n)
    anagram += w[0]
    w = w[1:]

print(anagram)