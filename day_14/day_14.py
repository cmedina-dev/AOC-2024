import numpy as np

def check_consecutive_ones(arr, count):
    for row in arr:
        consecutive_count = 0
        for element in row:
            if element == 1:
                consecutive_count += 1
                if consecutive_count >= count:
                    return True
            else:
                consecutive_count = 0
    return False

def move(arr, bot):
    row = bot[0]
    col = bot[1]
    dr = bot[2]
    dc = bot[3]
    new_row = (row + dr) % len(arr)
    new_col = (col + dc) % len(arr[0])
    arr[row][col] -= 1
    arr[new_row][new_col] += 1
    bot[0] = new_row
    bot[1] = new_col
    return arr, bot

data = [line.strip() for line in open('input.txt').readlines()]
matrix = [[0 for _ in range(101)] for _ in range(103)]
bots = []
for d in data:
    p, v = d.split()
    p = p.split('=')[1]
    p_c, p_r = map(int, p.split(','))
    v = v.split('=')[1]
    v_c, v_r = map(int, v.split(','))
    bot = [p_r, p_c, v_r, v_c]
    bots.append(bot)
    matrix[p_r][p_c] += 1
for t in range(100000):
    print(t)
    for bot in bots:
        matrix, bot = move(matrix, bot)
    tester = np.array(matrix)
    if check_consecutive_ones(tester, 10):
        print(t)
        for m in matrix:
            print(''.join(map(str, m)))
        break

q_1 = q_2 = q_3 = q_4 = 0
rows = len(matrix)
cols = len(matrix[0])
mid_row = rows // 2
mid_col = cols // 2

for r in range(rows):
    for c in range(cols):
        if r == mid_row and rows % 2 != 0:
            continue
        if c == mid_col and cols % 2 != 0:
            continue

        if r < mid_row and c < mid_col:
            q_1 += matrix[r][c]
        elif r < mid_row and c > mid_col:
            q_2 += matrix[r][c]
        elif r > mid_row and c < mid_col:
            q_3 += matrix[r][c]
        elif r > mid_row and c > mid_col:
            q_4 += matrix[r][c]
print(q_1, q_2, q_3, q_4)
print(q_1 * q_2 * q_3 * q_4)