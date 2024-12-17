import hashlib, numpy as np
from colorama import Fore, Back, Style
np.set_printoptions(edgeitems=30, linewidth=100000,
    formatter=dict(float=lambda x: "%.3g" % x))
def md5(x):
    return hashlib.md5(str.encode(x)).hexdigest()

def rotate_zone(move, robot, zone):
    row, col = robot
    if move == '<':
        path = zone[row, 0:col+1]
        if np.any(path == '.'):
            col_ptr = col - 1
            if zone[row, col_ptr] == '#': return
            while path[col_ptr] != '.':
                if path[col_ptr] == '#': return
                col_ptr -= 1
            shift_ptr = col_ptr + 1
            while zone[row, shift_ptr] != '@':
                zone[row, col_ptr] = zone[row, shift_ptr]
                shift_ptr += 1
                col_ptr += 1
            zone[row, col_ptr] = zone[row, shift_ptr]
            zone[row, shift_ptr] = '.'
    elif move == '>':
        path = zone[row, col:]
        offset = len(zone[0]) - len(path)
        if np.any(path == '.'):
            col_ptr = col - offset
            if zone[row, col_ptr + offset] == '#': return
            while path[col_ptr] != '.':
                if path[col_ptr] == '#': return
                col_ptr += 1
            shift_ptr = col_ptr - 1
            while zone[row, shift_ptr + offset] != '@':
                zone[row, col_ptr + offset] = zone[row, shift_ptr + offset]
                shift_ptr -= 1
                col_ptr -= 1
            zone[row, col_ptr + offset] = zone[row, shift_ptr + offset]
            zone[row, shift_ptr + offset] = '.'
    elif move == '^':
        path = zone[0:row+1, col]
        if np.any(path == '.'):
            row_ptr = row - 1
            if zone[row_ptr, col] == '#': return
            while path[row_ptr] != '.':
                if path[row_ptr] == '#': return
                row_ptr -= 1
            shift_ptr = row_ptr + 1
            while zone[shift_ptr, col] != '@':
                zone[row_ptr, col] = zone[shift_ptr, col]
                shift_ptr += 1
                row_ptr += 1
            zone[row_ptr, col] = zone[shift_ptr, col]
            zone[shift_ptr, col] = '.'
    elif move == 'v':
        path = zone[row:, col]
        offset = len(zone) - len(path)
        if np.any(path == '.'):
            row_ptr = row - offset
            if zone[row_ptr + offset, col] == '#': return
            while path[row_ptr] != '.':
                if path[row_ptr] == '#': return
                row_ptr += 1
            shift_ptr = row_ptr - 1
            while zone[shift_ptr + offset, col] != '@':
                zone[row_ptr + offset, col] = zone[shift_ptr + offset, col]
                shift_ptr -= 1
                row_ptr -= 1
            zone[row_ptr + offset, col] = zone[shift_ptr + offset, col]
            zone[shift_ptr + offset, col] = '.'
    return

def rotate_zone_p2(move, robot, zone):
    row, col = robot
    if move == '<':
        path = zone[row, 0:col+1]
        if np.any(path == '.'):
            col_ptr = col - 1
            if zone[row, col_ptr] == '#': return
            while path[col_ptr] != '.':
                if path[col_ptr] == '#': return
                col_ptr -= 1
            shift_ptr = col_ptr + 1
            while zone[row, shift_ptr] != '@':
                zone[row, col_ptr] = zone[row, shift_ptr]
                shift_ptr += 1
                col_ptr += 1
            zone[row, col_ptr] = zone[row, shift_ptr]
            zone[row, shift_ptr] = '.'
    elif move == '>':
        path = zone[row, col:]
        offset = len(zone[0]) - len(path)
        if np.any(path == '.'):
            col_ptr = col - offset
            if zone[row, col_ptr + offset] == '#': return
            while path[col_ptr] != '.':
                if path[col_ptr] == '#': return
                col_ptr += 1
            shift_ptr = col_ptr - 1
            while zone[row, shift_ptr + offset] != '@':
                zone[row, col_ptr + offset] = zone[row, shift_ptr + offset]
                shift_ptr -= 1
                col_ptr -= 1
            zone[row, col_ptr + offset] = zone[row, shift_ptr + offset]
            zone[row, shift_ptr + offset] = '.'
    elif move == '^':
        if zone[row-1, col] == '[' or zone[row-1, col] == ']':
            boxes = list()
            coords_to_check = list()
            row_ptr = row - 1
            if zone[row_ptr, col] == ']':
                box = ((row_ptr, col), (row_ptr, col - 1))
                boxes.append(box)
                coords_to_check.append((box[0][0]-1, box[0][1]))
                coords_to_check.append((box[1][0]-1, box[1][1]))
            elif zone[row_ptr, col] == '[':
                box = ((row_ptr, col), (row_ptr, col + 1))
                boxes.append(box)
                coords_to_check.append((box[0][0]-1, box[0][1]))
                coords_to_check.append((box[1][0]-1, box[1][1]))

            while len(coords_to_check) > 0:
                row, col = coords_to_check.pop()
                if zone[row, col] == '[':
                    box = ((row, col), (row, col + 1))
                    if not box in boxes and not tuple(reversed(box)) in boxes:
                        boxes.append(box)
                    coords_to_check.append((box[0][0] - 1, box[0][1]))
                    coords_to_check.append((box[1][0] - 1, box[1][1]))
                elif zone[row, col] == ']':
                    box = ((row, col), (row, col - 1))
                    if not box in boxes and not tuple(reversed(box)) in boxes:
                        boxes.append(box)
                    coords_to_check.append((box[0][0] - 1, box[0][1]))
                    coords_to_check.append((box[1][0] - 1, box[1][1]))

            can_move = True
            for box in boxes:
                coord_to_check_a = (box[0][0] - 1, box[0][1])
                coord_to_check_b = (box[1][0] - 1, box[1][1])
                if zone[coord_to_check_a] == '#' or zone[coord_to_check_b] == '#':
                    can_move = False
            if not can_move:
                return
            boxes = sorted(boxes, key=lambda box: box[0][0])

            for box in boxes:
                left = box[0]
                right = box[1]
                l_row, l_col = left
                r_row, r_col = right
                zone[l_row-1, l_col] = zone[l_row, l_col]
                zone[r_row-1, r_col] = zone[r_row, r_col]
                zone[l_row, l_col] = '.'
                zone[r_row, r_col] = '.'

        if zone[robot[0]-1, robot[1]] == '#': return
        zone[robot[0], robot[1]] = '.'
        zone[robot[0]-1, robot[1]] = '@'
    elif move == 'v':
        if zone[row+1, col] == '[' or zone[row+1, col] == ']':
            boxes = list()
            coords_to_check = list()
            row_ptr = row + 1
            if zone[row_ptr, col] == ']':
                box = ((row_ptr, col), (row_ptr, col - 1))
                boxes.append(box)
                coords_to_check.append((box[0][0]+1, box[0][1]))
                coords_to_check.append((box[1][0]+1, box[1][1]))
            elif zone[row_ptr, col] == '[':
                box = ((row_ptr, col), (row_ptr, col + 1))
                boxes.append(box)
                coords_to_check.append((box[0][0]+1, box[0][1]))
                coords_to_check.append((box[1][0]+1, box[1][1]))

            while len(coords_to_check) > 0:
                row, col = coords_to_check.pop()
                if zone[row, col] == '[':
                    box = ((row, col), (row, col + 1))
                    if not box in boxes and not tuple(reversed(box)) in boxes:
                        boxes.append(box)
                    coords_to_check.append((box[0][0] + 1, box[0][1]))
                    coords_to_check.append((box[1][0] + 1, box[1][1]))
                elif zone[row, col] == ']':
                    box = ((row, col), (row, col - 1))
                    if not box in boxes and not tuple(reversed(box)) in boxes:
                        boxes.append(box)
                    coords_to_check.append((box[0][0] + 1, box[0][1]))
                    coords_to_check.append((box[1][0] + 1, box[1][1]))

            can_move = True
            for box in boxes:
                coord_to_check_a = (box[0][0] + 1, box[0][1])
                coord_to_check_b = (box[1][0] + 1, box[1][1])
                if zone[coord_to_check_a] == '#' or zone[coord_to_check_b] == '#':
                    can_move = False
            if not can_move:
                return

            boxes = sorted(boxes, key=lambda box: box[0][0], reverse=True)
            for box in boxes:
                left = box[0]
                right = box[1]
                l_row, l_col = left
                r_row, r_col = right
                zone[l_row+1, l_col] = zone[l_row, l_col]
                zone[r_row+1, r_col] = zone[r_row, r_col]
                zone[l_row, l_col] = '.'
                zone[r_row, r_col] = '.'

        if zone[robot[0]+1, robot[1]] == '#': return
        zone[robot[0], robot[1]] = '.'
        zone[robot[0]+1, robot[1]] = '@'
    return

def widen(zone):
    widened_zone = [[]]
    for row in range(len(zone)):
        for col in range(len(zone[row])):
            if zone[row, col] == '#':
                widened_zone[row].append('#')
                widened_zone[row].append('#')
            elif zone[row, col] == '.':
                widened_zone[row].append('.')
                widened_zone[row].append('.')
            elif zone[row, col] == 'O':
                widened_zone[row].append('[')
                widened_zone[row].append(']')
            elif zone[row, col] == '@':
                widened_zone[row].append('@')
                widened_zone[row].append('.')
        widened_zone.append([])
    widened_zone.pop()
    widened_zone = np.array(widened_zone)
    return widened_zone

def part_two():
    file = open('input.txt')
    zone = list()
    moves = list()
    is_map = True
    for line in file.readlines():
        if line == '\n': is_map = False
        elif is_map:
            zone.append(list(line.strip()))
        else:
            moves.append(list(line.strip()))

    zone = widen(np.array(zone))
    moves = np.array(moves).flatten()
    for move in moves:
        robot = np.argwhere(zone == '@').flatten()
        rotate_zone_p2(move, robot, zone)
    ans = 0
    for row in range(len(zone)):
        for col in range(len(zone[row])):
            if zone[row][col] == "[":
                ans += 100 * row + col
    for z in zone:
        print(''.join(z))
    print(ans)
part_two()

def part_one():
    file = open('input.txt')
    zone = list()
    moves = list()
    is_map = True
    for line in file.readlines():
        if line == '\n': is_map = False
        elif is_map:
            zone.append(list(line.strip()))
        else:
            moves.append(list(line.strip()))

    zone = np.array(zone)
    moves = np.array(moves).flatten()

    for move in moves:
        robot = np.argwhere(zone == '@').flatten()
        rotate_zone(move, robot, zone)

    ans = 0
    for row in range(len(zone)):
        for col in range(len(zone[row])):
            if zone[row, col] == 'O':
                ans += 100 * row + col
    print(ans)
