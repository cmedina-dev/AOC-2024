from functools import cache

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

def get_coords_directional(n):
    if n == 1:
        return 0, 1
    elif n == 2:
        return 0, 2
    elif n == 3:
        return 1, 0
    elif n == 4:
        return 1, 1
    elif n == 5:
        return 1, 2
    return -1, -1

def get_vertical_count(start_row, end_row):
    return "v" * (end_row - start_row) if end_row > start_row else "^" * (start_row - end_row)

def get_horizontal_count(start_col, end_col):
    return ">" * (end_col - start_col) if end_col > start_col else "<" * (start_col - end_col)

def create_path_numeric(i, j):
    start_row, start_col = get_coords_numeric(i)
    end_row, end_col = get_coords_numeric(j)
    v = get_vertical_count(start_row, end_row)
    h = get_horizontal_count(start_col, end_col)

    num_pad_coords = {
        7: (0, 0), 8: (0, 1), 9: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        1: (2, 0), 2: (2, 1), 3: (2, 2),
        0: (3, 1), 10: (3, 2)
    }
    num_pad_rc = {v: k for k, v in num_pad_coords.items()}

    target_row, target_column = num_pad_coords[j]
    start_row, start_column = num_pad_coords[i]

    """Generate an L-shaped path to avoid excess movement. 
    Unsure why, but vertical moves are prioritized when moving left-to-right if the intermediate move is valid.
    Similarly, when moving right-to-left, horizontal moves are preferred when valid.
    (target_row, start_column) and (start_row, target_column) check intermediate moves to avoid gaps in the pads.
    Falls back to vertical movement for edge cases (e.g. 0->1 which is left-to-right, but requires vertical movement).
    """
    if end_col - start_col > 0 and (target_row, start_column) in num_pad_rc:
        return v + h + 'A'
    elif (start_row, target_column) in num_pad_rc:
        return h + v + 'A'
    else:
        return v + h + 'A'

def create_path_directional(i, j):
    start_row, start_col = get_coords_directional(i)
    end_row, end_col = get_coords_directional(j)
    v = get_vertical_count(start_row, end_row)
    h = get_horizontal_count(start_col, end_col)

    dir_pad_coords = {
        1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
    }
    dir_pad_rc = {v: k for k, v in dir_pad_coords.items()}

    start_row, start_col = dir_pad_coords[i]
    target_row, target_col = dir_pad_coords[j]

    if end_col - start_col > 0 and (target_row, start_col) in dir_pad_rc:
        return v + h + 'A'
    elif (start_row, target_col) in dir_pad_rc:
        return h + v + 'A'
    else:
        return v + h + 'A'

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

@cache
def compute_seq(seq, n=1):
    ans = 0
    if n == 0: return len(seq)
    for i in range(len(seq)):
        if i == 0:
            ans += compute_seq(directional_lut['A'][seq[i]], n-1)
        else:
            ans += compute_seq(directional_lut[seq[i - 1]][seq[i]], n-1)
    return ans

ans = 0
for i in range(len(seqs)):
    temp = compute_seq(seqs[i], n=25)
    ans += (int(f[i][:3]) * temp)
print(ans)