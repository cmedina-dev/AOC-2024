import copy, heapq, numpy as np

def dijkstra(maze, s, e):
    heap = []
    distance = [[float('inf') for _ in range(len(maze))] for _ in range(len(maze))]
    distance[s[0]][s[1]] = 0
    visited = [[False for _ in range(len(maze))] for _ in range(len(maze))]
    vec = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heapq.heappush(heap, (0, s))

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        visited[cur_node[0]][cur_node[1]] = True
        if maze[cur_node[0]][cur_node[1]] == 'E': return cur_dist

        for v in vec:
            neighbor_node = (cur_node[0] + v[0], cur_node[1] + v[1])
            if visited[neighbor_node[0]][neighbor_node[1]]: continue
            if maze[neighbor_node[0]][neighbor_node[1]] == '#': continue

            new_dist = cur_dist + 1
            if new_dist < distance[neighbor_node[0]][neighbor_node[1]]:
                distance[neighbor_node[0]][neighbor_node[1]] = cur_dist + 1
                heapq.heappush(heap, (distance[neighbor_node[0]][neighbor_node[1]], neighbor_node))
    return -1


maze = np.array([list(item.strip()) for item in open("input.txt").readlines()])
start = np.argwhere(maze == 'S')[0]
end = np.argwhere(maze == 'E')[0]
print(maze)
to_check = []

for row in range(1, len(maze)-1):
    for col in range(1, len(maze[row])-1):
        if maze[row, col] == '#':
            new_maze = copy.deepcopy(maze)
            new_maze[row, col] = '.'
            to_check.append(new_maze)

base_dist = dijkstra(maze, start, end)
times_saved = {}

for k, v in enumerate(to_check):
    print(f'On maze {k} of {len(to_check)}')
    dist = dijkstra(v, start, end)
    time_saved = base_dist - dist
    if time_saved < 100: continue
    if not time_saved in times_saved:
        times_saved[time_saved] = 1
    else:
        times_saved[time_saved] += 1
print(sum(times_saved.values()))