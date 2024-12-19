import numpy as np
import heapq
np.set_printoptions(edgeitems=30, linewidth=100000,
    formatter=dict(float=lambda x: "%.3g" % x))

data = open('input.txt')
maze = np.array([list(line.strip()) for line in data.readlines()])
dist = np.array([[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))])
visited = np.array([['?' for _ in range(len(maze[0]))] for _ in range(len(maze))])
previous = np.array([[[] for _ in range(len(maze[0]))] for _ in range(len(maze))])
start = np.argwhere(maze == 'S')[0]
dist[start[0], start[1]] = 0
end = np.argwhere(maze == 'E')[0]
vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
start_vec = (1, 0)
heap = []
heapq.heappush(heap, (0, start, start_vec))
while heap:
    cur_dist, cur_pos, cur_vec = heapq.heappop(heap)
    if visited[cur_pos[0], cur_pos[1]] == '*': continue
    visited[cur_pos[0], cur_pos[1]] = '*'
    for v in vec:
        neighbor_row, neighbor_col = cur_pos[0] + v[0], cur_pos[1] + v[1]
        if 0 <= neighbor_row < len(maze) and 0 <= neighbor_col < len(maze[0]):
            if visited[neighbor_row, neighbor_col] == '*': continue
            if maze[neighbor_row, neighbor_col] == '#': continue
            new_dist = cur_dist + 1
            if cur_vec == (1, 0) or cur_vec == (-1, 0):
                if v == (0, 1) or v == (0, -1):
                    new_dist += 1000
            elif cur_vec == (0, 1) or cur_vec == (0, -1):
                if v == (1, 0) or v == (-1, 0):
                    new_dist += 1000
            if new_dist <= dist[neighbor_row, neighbor_col]:
                dist[neighbor_row, neighbor_col] = new_dist
                previous[neighbor_row, neighbor_col].append(cur_pos)
                heapq.heappush(heap, (new_dist, (neighbor_row, neighbor_col), v))

path = []
cur = (end[0], end[1])
while cur is not None:
    path.append(cur)
    cur = previous[cur[0], cur[1]]
path.reverse()
f_a = path[0]
f_b = path[1]
(v1, v2) = f_a - f_b
if (v1, v2) == (-1, 0) or (v1, v2) == (1, 0):
    dist[end[0], end[1]] += 1000
else:
    dist[end[0], end[1]] -= 1000
print(int(dist[end[0], end[1]]))
print(len(path))

maze_traveled = maze.copy()
for p in path:
    row, col = p
    maze_traveled[row][col] = '*'
