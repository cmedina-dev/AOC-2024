import heapq, numpy as np

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def dijkstra(maze, s):
    heap = []
    distance = [[float('inf') for _ in range(len(maze))] for _ in range(len(maze))]
    distance[s[0]][s[1]] = 0
    visited = [[False for _ in range(len(maze))] for _ in range(len(maze))]
    vec = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heapq.heappush(heap, (0, s))
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        visited[cur_node[0]][cur_node[1]] = True
        for v in vec:
            neighbor_node = (cur_node[0] + v[0], cur_node[1] + v[1])
            if visited[neighbor_node[0]][neighbor_node[1]]: continue
            if maze[neighbor_node[0]][neighbor_node[1]] == '#': continue
            new_dist = cur_dist + 1
            if new_dist < distance[neighbor_node[0]][neighbor_node[1]]:
                distance[neighbor_node[0]][neighbor_node[1]] = cur_dist + 1
                heapq.heappush(heap, (distance[neighbor_node[0]][neighbor_node[1]], neighbor_node))
    return distance

maze = np.array([list(item.strip()) for item in open("input.txt").readlines()])
start = np.argwhere(maze == 'S')[0]
distances = np.array(dijkstra(maze, start))
valid_points = np.array(sorted(np.argwhere(distances != float('inf')), key=lambda x: distances[x[0]][x[1]]))
times = {}
for i in range(len(valid_points)):
    for j in range(i+1, len(valid_points)):
        x1 = valid_points[i][0]
        x2 = valid_points[j][0]
        y1 = valid_points[i][1]
        y2 = valid_points[j][1]
        dist_start = distances[x1][y1]
        dist_end = distances[x2][y2]
        manhattan_dist = manhattan(x1, y1, x2, y2)
        if manhattan_dist > 20: continue
        elif dist_end - dist_start < 30: continue

        time_saved = int(dist_end - dist_start - manhattan_dist)
        if time_saved < 30: continue

        if not time_saved in times:
            times[time_saved] = 1
        else:
            times[time_saved] += 1
print(times)
print(sum(times.values()))