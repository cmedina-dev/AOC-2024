rules = []
pages = []
rules_ = True
with open('input.txt', 'r') as f:
    for line in f.readlines():
        d = line.strip()
        if len(d) == 0:
            rules_ = False
            continue
        if rules_:
            rules.append(d)
        else:
            pages.append(d)

lefts = set()
rights = set()
children = dict()

# Isolate the root value
for r in rules:
    r_ = r.split('|')
    lefts.add(r_[0])
    rights.add(r_[1])
    if r_[1] in children:
        children[r_[1]].append(r_[0])
    else:
        children[r_[1]] = list()
        children[r_[1]].append(r_[0])

orders = list(rights.difference(lefts))

def check_page(page, p2=False):
    prev = []
    for p in page:
        if len(prev) == 0:
            prev.append(p)
            continue
        for p_ in prev:
            if p_ in children:
                for p__ in children[p_]:
                    if p__ == p:
                        if p2: return p_, p
                        return False
        prev.append(p)
    return True

def reorder(page, p1, p2):
    t = page.index(p1)
    t_ = page.index(p2)
    page[t] = p2
    page[t_] = p1
    return page

def part_one():
    ans = 0
    for p in pages:
        p_ = p.split(',')
        if check_page(p_):
            ans += int(p_[len(p_) // 2])
    print(ans)
part_one()

def part_two():
    ans = 0
    for p in pages:
        p_ = p.split(',')
        c = check_page(p_, True)
        adds = False
        if c is not True:
            adds = True
        while c is not True:
            p1 = c[0]
            p2 = c[1]
            p_ = reorder(p_, p1, p2)
            c = check_page(p_, True)
        if adds: ans += int(p_[len(p_) // 2])
    print(ans)
part_two()
