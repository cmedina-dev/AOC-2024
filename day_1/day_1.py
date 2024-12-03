import sys, cProfile, pstats, io
import numpy as np
sys.stdin = open('input.txt', 'r')
tokens = np.fromstring(sys.stdin.read(), sep=' ', dtype=int)
left = tokens[::2]
right = tokens[1::2]
left.sort()
right.sort()

def part_two():
    dist_t = np.sum(np.where(left in right, left * right.count(left), 0))
    print(dist_t)

def part_one():
    # Compute the sum of absolute differences
    dist_t = np.sum(np.abs(left - right))
    print(dist_t)

pr = cProfile.Profile()
pr.enable()
part_one()
part_two()
pr.disable()
s = io.StringIO()
sortby = pstats.SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())