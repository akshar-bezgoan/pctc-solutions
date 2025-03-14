import math
guests = int(input())
packets = math.ceil(guests/5)
batches = math.ceil(guests/7)
time = batches *11
print(packets,time)