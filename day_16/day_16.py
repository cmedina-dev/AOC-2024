import numpy as np
from collections import deque
np.set_printoptions(edgeitems=30, linewidth=100000,
    formatter={'all': lambda x: f'{x:12}'})

data = open('input.txt')
maze = np.array([list(line.strip()) for line in data.readlines()])
dist = np.array([[float('inf') for _ in range(maze.shape[1])] for _ in range(maze.shape[0])])
start = np.argwhere(maze == 'S')[0]
end = np.argwhere(maze == 'E')[0]
vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
start_vec = (1, 0)
visited = set()

q = deque()
dist[start[0], start[1]] = 0
cur_vec = (0, 1)
q.append(((start[0], start[1]), cur_vec))

while q:
    node, cur_vec = q.popleft()
    if (node[0], node[1]) == (end[0], end[1]):
        print('Found!')
        continue
    for v in vec:
        neighbor = (node[0] + v[0], node[1] + v[1])
        if maze[neighbor[0], neighbor[1]] != '#':
            d = dist[neighbor[0], neighbor[1]]
            if dist[node[0], node[1]] + 1 > d: continue
            if d == float('inf'):
                dist[neighbor[0], neighbor[1]] = dist[node[0], node[1]] + 1
                if cur_vec == (1,0) or cur_vec == (-1,0):
                    if v == (0,1) or v == (0,-1):
                        dist[neighbor[0], neighbor[1]] += 1000
                elif cur_vec == (0,1) or cur_vec == (0,-1):
                    if v == (1,0) or v == (-1,0):
                        dist[neighbor[0], neighbor[1]] += 1000
            visited.add((node[0], node[1]))
            q.append((neighbor, v))
print(dist)