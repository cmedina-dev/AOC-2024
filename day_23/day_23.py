import itertools
pairs = set(tuple(line.strip().split('-')) for line in open('input.txt'))
t = set(pair for pair in pairs if any(c[0]=='t' for c in pair))
t_table = {}
for t_ in t:
    if t_[0][0] == 't':
        if not t_[0] in t_table:
            t_table[t_[0]] = [t_[1]]
        else:
            t_table[t_[0]].append(t_[1])
    elif t_[1][0] == 't':
        if not t_[1] in t_table:
            t_table[t_[1]] = [t_[0]]
        else:
            t_table[t_[1]].append(t_[0])
ans = 0
for _, item in enumerate(t_table.items()):
    conn = item[1]
    for p in list(itertools.permutations(conn, 2)):
        if p in pairs:
            ans += 1
print(ans)