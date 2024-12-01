import sys
sys.stdin = open('input.txt', 'r')
data = sys.stdin.read().splitlines()


def part_two():
    left = []
    right = []
    for line in data:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()
    dist_t = 0

    for i in range(len(left)):
        left[i] *= right.count(left[i])
        dist_t += left[i]

    print(dist_t)

part_two()

def part_one():
    left = []
    right = []
    for line in data:
        l, r = line.split()
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    dist_t = 0

    for i in range(len(left)):
        dist = abs(int(left[i]) - int(right[i]))
        dist_t += dist

    print(dist_t)