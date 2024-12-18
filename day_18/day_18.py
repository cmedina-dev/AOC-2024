import numpy as np
import heapq
np.set_printoptions(edgeitems=30, linewidth=100000,
    formatter=dict(float=lambda x: "%.3g" % x))

def solve(maze):
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    vec = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    found = False
    dist = np.array([[float("inf") for _ in range(71)] for _ in range(71)])
    visited = np.array([[False for _ in range(71)] for _ in range(71)])

    while heap:
        cur_dist, cur_row, cur_col = heapq.heappop(heap)
        if visited[cur_row, cur_col]: continue
        visited[cur_row, cur_col] = True

        if (cur_row, cur_col) == end:
            print(dist[70, 70])
            return True
        for delta_row, delta_col in vec:
            neighbor_row, neighbor_col = cur_row + delta_row, cur_col + delta_col
            if 0 <= neighbor_row <= 70 and 0 <= neighbor_col <= 70:
                if maze[neighbor_row, neighbor_col] == '.' and not visited[neighbor_row, neighbor_col]:
                    new_dist = cur_dist + 1
                    if new_dist < dist[neighbor_row, neighbor_col]:
                        dist[neighbor_row, neighbor_col] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor_row, neighbor_col))
    if not found:
        return False

file = open('input.txt')
bad = file.readlines()
maze = np.array([["." for _ in range(71)] for _ in range(71)])
end = (70, 70)
byte_count = 0
for b in bad:
    if byte_count == 1025: break
    row, col = list(map(int, b.split(",")))
    maze[row, col] = "#"
    byte_count += 1
ptr = 1024

solved = solve(maze)
while solved:
    ptr += 1
    row, col = list(map(int, bad[ptr].split(",")))
    print(row, col)
    maze[row, col] = "#"
    solved = solve(maze)
print(ptr)