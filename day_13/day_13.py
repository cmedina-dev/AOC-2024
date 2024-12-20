inputs = open('input.txt').read().split('\n\n')
for i in inputs:
    line = i.split('\n')
    a_x, a_y = line.split(': ')
