n = int(input())
name = ''
max = 0
mxc = 0
for i in range(n):
    temp_name, colour, bw = input().split()
    colour, bw = int(colour), int(bw)
    if 2*colour + bw > max:
        name = temp_name
        max = 2*colour + bw
        mxc = colour
    elif 2*colour +bw == max:
        if colour > mxc:
            name = temp_name
            max = 2*colour + bw
            mxc = colour

print(name)