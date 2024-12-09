import numpy as np, itertools as it
f = open('input.txt')
d = np.array([list(line.strip()) for line in f])

def is_freq(c):
    return c != '.' and c != '#'

def part_two():
    d_ = d.copy()
    freq = set()
    for row in range(len(d_)):
        for col in range(len(d_[row])):
            if is_freq(d_[row, col]):
                freq.add((str(d_[row, col]), row, col))

    freq = sorted(list(freq), key=lambda x: ord(x[0]))
    freq_ = list()
    coords = set()
    for k, g in it.groupby(freq, key=lambda x: ord(x[0])):
        freq_.append(sorted(list(g)))
    for j in freq_:
        for jj in j:
            coords.add((jj[1], jj[2]))
    for f_ in freq_:
        p = list(it.combinations(f_, 2))
        for p_ in p:
            d1_row = p_[0][1]
            d1_col = p_[0][2]
            d2_row = p_[1][1]
            d2_col = p_[1][2]
            delta_row = abs(d2_row - d1_row)
            delta_col = abs(d2_col - d1_col)
            if d1_col == d2_col:
                slope = 0
            else:
                slope = -((d2_row - d1_row) / (d2_col - d1_col))
            if slope > 0:
                anode_1_row = d1_row - delta_row
                anode_1_col = d1_col + delta_col
                anode_2_row = d2_row + delta_row
                anode_2_col = d2_col - delta_col
                d_[d1_row, d1_col] = '#'
                d_[d2_row, d2_col] = '#'
                while 0 <= anode_1_row < len(d_) and 0 <= anode_1_col < len(d_[0]):
                    d_[anode_1_row, anode_1_col] = '#'
                    anode_1_row -= delta_row
                    anode_1_col += delta_col
                while 0 <= anode_2_row < len(d_) and 0 <= anode_2_col < len(d_[0]):
                    d_[anode_2_row, anode_2_col] = '#'
                    anode_2_row += delta_row
                    anode_2_col -= delta_col
            elif slope < 0:
                anode_1_row = d1_row - delta_row
                anode_1_col = d1_col - delta_col
                anode_2_row = d2_row + delta_row
                anode_2_col = d2_col + delta_col
                d_[d1_row, d1_col] = '#'
                d_[d2_row, d2_col] = '#'
                while 0 <= anode_1_row < len(d_) and 0 <= anode_1_col < len(d_[0]):
                    d_[anode_1_row, anode_1_col] = '#'
                    anode_1_row -= delta_row
                    anode_1_col -= delta_col
                while 0 <= anode_2_row < len(d_) and 0 <= anode_2_col < len(d_[0]):
                    d_[anode_2_row, anode_2_col] = '#'
                    anode_2_row += delta_row
                    anode_2_col += delta_col
    antinode_count = 0
    for i in range(len(d_)):
        for j in range(len(d_[i])):
            if d_[i][j] == '#':
                antinode_count += 1
    print(antinode_count)
part_two()

def part_one():
    freq = set()
    for row in range(len(d)):
        for col in range(len(d[row])):
            if is_freq(d[row,col]):
                freq.add((str(d[row,col]), row,col))

    freq = sorted(list(freq), key=lambda x: ord(x[0]))
    freq_ = list()
    for k, g in it.groupby(freq, key=lambda x: ord(x[0])):
        freq_.append(sorted(list(g)))
    for f_ in freq_:
        p = list(it.combinations(f_, 2))
        for p_ in p:
            d1_row = p_[0][1]
            d1_col = p_[0][2]
            d2_row = p_[1][1]
            d2_col = p_[1][2]
            delta_row = abs(d2_row - d1_row)
            delta_col = abs(d2_col - d1_col)
            if d1_col == d2_col:
                slope = 0
            else:
                slope = -((d2_row - d1_row) / (d2_col - d1_col))
            if slope > 0:
                anode_1_row = d1_row - delta_row
                anode_1_col = d1_col + delta_col
                anode_2_row = d2_row + delta_row
                anode_2_col = d2_col - delta_col
                if 0 <= anode_1_row < len(d) and 0 <= anode_1_col < len(d[0]):
                    d[anode_1_row, anode_1_col] = '#'
                if 0 <= anode_2_row < len(d) and 0 <= anode_2_col < len(d[0]):
                    d[anode_2_row, anode_2_col] = '#'
            elif slope < 0:
                anode_1_row = d1_row - delta_row
                anode_1_col = d1_col - delta_col
                anode_2_row = d2_row + delta_row
                anode_2_col = d2_col + delta_col
                if 0 <= anode_1_row < len(d) and 0 <= anode_1_col < len(d[0]):
                    d[anode_1_row, anode_1_col] = '#'
                if 0 <= anode_2_row < len(d) and 0 <= anode_2_col < len(d[0]):
                    d[anode_2_row, anode_2_col] = '#'
    antinode_count = 0
    for i in range(len(d)):
        for j in range(len(d[i])):
            if d[i][j] == '#':
                antinode_count += 1
    print(antinode_count)
part_one()