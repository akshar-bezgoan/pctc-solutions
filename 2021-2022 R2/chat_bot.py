inp = input()
while inp != 'goodbye':
    if inp.split()[0] == 'how' or inp.split()[0] == 'what' or inp.split()[0] == 'why' or inp.split()[0] == 'who' or inp.split()[0] == 'when' or inp.split()[0] == 'where' or inp[-1] == '?':
        print('not sure really')
    else:
        print('but why?')
    inp = input()
print('see you!')


'''
my name is dijanna
that's what my parents called me
are you real?
how can anyone tell anyway
whoever they are
goodbye
'''