f = open('input.txt').read()
n = list()
id = 0
free_spans = list()

def update_spans(s):
    spans = []
    l = 0
    count = 0
    start = None

    for _, char in enumerate(s):
        if char == '.':
            if count == 0:
                start = l
            count += 1
        else:
            if count > 0:
                spans.append((start, count))
                count = 0
        l += 1
    if count > 0:
        spans.append((start, count))
    return sorted(spans, key=lambda x: x[0])

for i in range(0, len(f), 2):
    file = f[i:i+1]
    free = f[i+1:i+2]
    for _ in range(int(file)):
        n.append(str(id))
    if free:
        for _ in range(int(free)):
            n.append('.')
    id += 1

free_spans = update_spans(n)
r = len(n)-1
id -= 1

while r >= 0 and id > 0:
    if r % 100 == 0:
        print(r)
    seq_idx = n.index(str(id))
    span_len = 0
    l = seq_idx
    while l < len(n) and n[l] == str(id):
        span_len += 1
        l += 1
    swap_idx = None
    for s in free_spans:
        if s[1] >= span_len:
            swap_idx = s[0]
            break
    if swap_idx is None:
        free_spans = update_spans(n[:seq_idx])
        r -= 1
        id -= 1
        continue
    n[swap_idx:swap_idx+span_len], n[seq_idx:seq_idx+span_len] = n[seq_idx:seq_idx+span_len], n[swap_idx:swap_idx+span_len]
    free_spans = update_spans(n[:seq_idx])
    id -= 1
    r = seq_idx

pos = 0
ans = 0
for v in n:
    if v == '.':
        pos += 1
        continue
    ans += int(v) * pos
    pos += 1
print(ans)