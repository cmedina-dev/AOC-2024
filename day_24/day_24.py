from collections import defaultdict, deque

values = [item.strip() for item in open('input.txt').read().split('\n\n')]
registers = defaultdict(int)
print(values)
for item in values[0].split('\n'):
    print(item)
    k, v = item.split(': ')
    registers[k] = int(v)

instruct_lut = {
    'AND' : lambda x, y: x & y,
    'OR' : lambda x, y: x | y,
    'XOR' : lambda x, y: x ^ y,
}
queue = deque()
for instruct in values[1].split('\n'):
    a, op, b, _, c = instruct.split()
    if a not in registers or b not in registers:
        queue.append((a, op, b, c))
        continue
    registers[c] = instruct_lut[op](registers[a], registers[b])
while len(queue) > 0:
    a, op, b, c = queue.popleft()
    if a not in registers or b not in registers:
        queue.append((a, op, b, c))
        continue
    registers[c] = instruct_lut[op](registers[a], registers[b])
z = sorted([(item, registers[item]) for item in registers if item[0] == 'z'], key=lambda x: int(x[0][1:]), reverse=True)
print(int(''.join([str(zz[1]) for zz in z]), 2))