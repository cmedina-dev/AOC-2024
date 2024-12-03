import re

f = open('input.txt')
data = f.read().splitlines()

def part_two():
    pattern = re.compile(r'(?:mul\({1}[0-9]{1,3},{1}[0-9]{1,3}\))|(?:do\({1}\){1})|(?:don\'{1}t\({1}\){1})')
    sums = 0
    disabled = False
    for line in data:
        m = re.findall(pattern, line)
        for x in m:
            if x == "don't()":
                disabled = True
            elif x == "do()":
                disabled = False
            elif not disabled:
                mul = x.split('(')
                mul_ = mul[1].split(',')
                mul_[1] = mul_[1].replace(')', '')
                l = int(mul_[0])
                r = int(mul_[1])
                a = l * r
                sums += a
    print(sums)

part_two()

def part_one():
    pattern = re.compile(r'(?:mul\({1}[0-9]{1,3},{1}[0-9]{1,3}\))')
    sums = 0
    for line in data:
        m = re.findall(pattern, line)
        for x in m:
            mul = x.split('(')
            mul_ = mul[1].split(',')
            mul_[1] = mul_[1].replace(')','')
            l = int(mul_[0])
            r = int(mul_[1])
            a = l * r
            sums += a
    print(sums)