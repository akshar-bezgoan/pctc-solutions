from math import factorial

s = input()
index = int(input()) 
total = len(s)
def get_counts(string):
    count = {}
    for i in string:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

count = get_counts(s)

def num_dupes():
    dupes = 1
    for i in count:
        dupes *= factorial(count[i])
    return dupes

dupes = num_dupes()
n_perms = int(factorial(total)/dupes)

def strict_perm(letter):
    dupes = num_dupes()
    n = count[letter]
    perm = n * (factorial(total-1)) // dupes
    return perm

if index == 1:
    ans = s
elif index == n_perms:
    ans = s[::-1]
else:
    ans = ''
    for i in range(len(s)):
        for i in range(len(list(count.keys()))):
            curr = list(count.keys())[i]
            perm = strict_perm(curr)
            if perm < index:
                index -= perm
            else:
                ans += curr
                count[curr] -= 1
                total -= 1
                if count[curr] == 0:
                    del count[curr]
                break
print(ans)