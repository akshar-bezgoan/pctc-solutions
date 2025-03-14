hometime = int(input())
bedtime = int(input())-1
hws = int(input()) * 35
dinner = int(input())
freetime = (bedtime-hometime)*60
print(max(0, freetime - (hws + dinner)))