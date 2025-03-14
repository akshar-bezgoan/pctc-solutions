hws = int(input())
t = int(input()) #time in seconds
all_hw = []
for i in range(hws):
    all_hw.append(int(input()))

all_hw = sorted(all_hw)
finished = []
for i in range(len(all_hw)):
    if all_hw[i] <= t:
        t -= all_hw[i]
        finished.append(all_hw[i])

print(len(all_hw) - len(finished))