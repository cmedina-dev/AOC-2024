def bron_kerbosch(R, P, X, cliques):
    if not P and not X:
        cliques.append(R)
        return

    for v in list(P):
        neighbors = N.get(v, set())
        bron_kerbosch(R.union({v}), P.intersection(neighbors), X.intersection(neighbors), cliques)
        P.discard(v)
        X.add(v)

pairs = set()
for line in open('input.txt'):
    parts = line.strip().split('-')
    pairs.add((parts[0], parts[1]))
    pairs.add((parts[1], parts[0]))
N = {}
P = set()
for pair in pairs:
    u, v = pair
    if u not in N:
        N[u] = set()
    if v not in N:
        N[v] = set()
    N[u].add(v)
    N[v].add(u)

cliques = []
nodes = set(N.keys())
bron_kerbosch(set(), nodes, set(), cliques)
print(','.join(sorted(list(max(cliques, key=len)))))