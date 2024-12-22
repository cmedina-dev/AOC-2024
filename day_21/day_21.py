def get_coords_numeric(n):
    if n == 7:
        return 0, 0
    elif n == 8:
        return 0, 1
    elif n == 9:
        return 0, 2
    elif n == 4:
        return 1, 0
    elif n == 5:
        return 1, 1
    elif n == 6:
        return 1, 2
    elif n == 1:
        return 2, 0
    elif n == 2:
        return 2, 1
    elif n == 3:
        return 2, 2
    elif n == 0:
        return 3, 1
    elif n == 10:
        return 3, 2
    return -1, -1


def create_path_numeric(i, j):
    start_row, start_col = get_coords_numeric(i)
    end_row, end_col = get_coords_numeric(j)

    vert = "v" * (end_row - start_row) if end_row > start_row else "^" * (start_row - end_row)
    horiz = ">" * (end_col - start_col) if end_col > start_col else "<" * (start_col - end_col)

    num_pad_coords = {
        7: (0, 0), 8: (0, 1), 9: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        1: (2, 0), 2: (2, 1), 3: (2, 2),
        0: (3, 1), 10: (3, 2)
    }
    num_pad_rc = {v: k for k, v in num_pad_coords.items()}

    ti, tj = num_pad_coords[j]
    si, sj = num_pad_coords[i]

    if end_col - start_col > 0 and (ti, sj) in num_pad_rc:
        return vert + horiz + 'A'
    elif (si, tj) in num_pad_rc:
        return horiz + vert + 'A'
    else:
        return vert + horiz + 'A'

def create_path_directional(i, j):
    path = []
    i_row = j_row = i_col = j_col = -1
    if i == 1 or i == 2:
        i_row = 0
    elif i == 3 or i == 4 or i == 5:
        i_row = 1
    if i == 3:
        i_col = 0
    elif i == 1 or i == 4:
        i_col = 1
    elif i == 2 or i == 5:
        i_col = 2
    if j == 1 or j == 2:
        j_row = 0
    elif j == 3 or j == 4 or j == 5:
        j_row = 1
    if j == 3:
        j_col = 0
    elif j == 1 or j == 4:
        j_col = 1
    elif j == 2 or j == 5:
        j_col = 2
    while i_row != j_row or i_col != j_col:
        if i_col > j_col:
            i_col -= 1
            path.append('<')
        elif i_row > j_row:
            i_row -= 1
            path.append('^')
        elif i_row < j_row:
            i_row += 1
            path.append('v')
        elif i_col < j_col:
            i_col += 1
            path.append('>')
    return ''.join(path) + 'A'

numeric_lut = {}
for i in range(11):
    key = str(i)
    if i == 10: key = 'A'
    numeric_lut[key] = {}
    for j in range(11):
        sub_key = str(j)
        if i == j: continue
        if j == 10: sub_key = 'A'
        numeric_lut[key][sub_key] = create_path_numeric(i, j)
for key in numeric_lut:
    print(key, numeric_lut[key])
print()
directional_lut = {}
key = {
    1: '^',
    2: 'A',
    3: '<',
    4: 'v',
    5: '>',
}
for i in range(6):
    if i == 0: continue
    directional_lut[key[i]] = {}
    for j in range(6):
        if j == 0: continue
        directional_lut[key[i]][key[j]] = create_path_directional(i, j)
for key in directional_lut:
    print(key, directional_lut[key])


seqs = []
f = [line.strip() for line in open('input.txt').readlines()]
for item in f:
    chars = list(item)
    seqs.append(numeric_lut['A'][chars[0]] +
                numeric_lut[chars[0]][chars[1]] +
                numeric_lut[chars[1]][chars[2]] +
                numeric_lut[chars[2]][chars[3]])

def compute_seq(seq, n=1):
    print(n)
    if n == 0:
        print(seq)
        return len(seq)
    else:
        new_seq = []
        prev_c = -1
        for c in seq:
            if len(new_seq) == 0:
                new_seq.append(directional_lut['A'][c])
            else:
                new_seq.append(directional_lut[prev_c][c])
            prev_c = c
        new_seq = ''.join(new_seq)
        return compute_seq(new_seq, n - 1)

ans = 0
for i in range(len(seqs)):
    temp = compute_seq(seqs[i], n=25)
    ans += (int(f[i][:3]) * temp)
print(ans)