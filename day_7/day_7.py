from itertools import product, combinations, combinations_with_replacement, chain, zip_longest
import numpy as np
f = open('input.txt').readlines()
signs = ['+', '*', '||']

def part_two():
    goods = set()
    for line in f:
        l = line.strip()
        test, ops = l.split(':')
        ops = ops.split()
        e = list(product(signs, repeat=len(ops)-1))
        e_ = [tuple(reversed(x)) for x in e]
        d = list(set(chain(e, e_)))
        d = [list(x) for x in d]
        for d_ in d:
            g = np.array(list(zip_longest(ops, d_))).flatten()
            g = np.delete(g, -1)
            i = 2
            check = int(g[0])
            while i < len(g):
                match g[i-1]:
                    case '+':
                        check += int(g[i])
                    case '*':
                        check *= int(g[i])
                    case '||':
                        check = str(check)
                        check += g[i]
                        check = int(check)
                i += 2
            if check == int(test):
                goods.add(int(test))
    print(sum(goods))
part_two()

def part_one():
    goods = set()
    for line in f:
        l = line.strip()
        test, ops = l.split(':')
        if int(test) in goods: continue
        ops = ops.split()
        e = list(product(signs, repeat=len(ops)-1))
        e_ = [tuple(reversed(x)) for x in e]
        d = list(set(chain(e, e_)))
        d = [list(x) for x in d]
        for d_ in d:
            g = np.array(list(zip_longest(ops, d_))).flatten()
            g = np.delete(g, -1)
            i = 2
            check = int(g[0])
            while i < len(g):
                match g[i-1]:
                    case '+':
                        check += int(g[i])
                    case '*':
                        check *= int(g[i])
                i += 2
            if check == int(test):
                goods.add(int(test))
    print(sum(goods))