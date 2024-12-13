import copy

def get_perimeter(matrix):
    perimeter = 0
    row_l = 0
    col_l = 0
    row_r = 1
    col_r = 1
    patterns = {
        ((0, 0), (0, 1)),
        ((0, 0), (1, 0)),
        ((0, 1), (0, 0)),
        ((1, 0), (0, 0)),
        ((1, 1), (1, 0)),
        ((1, 1), (0, 1)),
        ((1, 0), (1, 1)),
        ((0, 1), (1, 1)),
        ((1, 0), (0, 1)),
        ((0, 1), (1, 0))
    }
    while row_r < len(matrix):
        while col_r < len(matrix[row_r]):
            pattern = ((matrix[row_l][col_l], matrix[row_l][col_r]), (matrix[row_r][col_l], matrix[row_r][col_r]))
            if pattern in patterns:
                perimeter += 1
                if pattern == ((1, 0), (0, 1)) or pattern == ((0, 1), (1, 0)):
                    perimeter += 1
            col_l += 1
            col_r += 1
        col_l = 0
        col_r = 1
        row_l += 1
        row_r += 1
    return perimeter

def isolate_block(start, matrix_, v, letter=None):
    vecs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    v.add(start)
    matrix_[start[0]][start[1]] = 1
    for vec in vecs:
        check = (start[0] + vec[0], start[1] + vec[1])
        if matrix_[check[0]][check[1]] == letter:
            if check in v: continue
            matrix_ = isolate_block(check, matrix_, v, letter)
    matrix_[start[0]][start[1]] = 1
    return matrix_

f = [list(line.strip('\n')) for line in open('input.txt', 'r').readlines()]
ff = [[0 for i in range(len(f)+2)] for j in range(len(f)+2)]

for i in range(len(ff)):
    for j in range(len(ff[i])):
        if 0 <= i < len(f) and 0 <= j < len(f[i]):
            if f[i][j] != 0:
                ff[i+1][j+1] = f[i][j]

visited = set()
matrix = copy.deepcopy(ff)
iso_blocks = list()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i, j) in visited or matrix[i][j] == 0:
            continue
        m_ = copy.deepcopy(matrix)
        for v in visited:
            m_[v[0]][v[1]] = 0
        iso_block = isolate_block((i, j), m_, set(), m_[i][j])
        iso_blocks.append(iso_block)
        for k in range(len(iso_block)):
            for l in range(len(iso_block[k])):
                if iso_block[k][l] == 1:
                    visited.add((k, l))
cost = 0
for block in iso_blocks:
    a = 0
    p = 0
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] != 1:
                block[i][j] = 0
            if block[i][j] == 1:
                a += 1
    p = get_perimeter(block)
    cost += p * a
print(cost)