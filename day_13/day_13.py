import sys
from functools import cache

sys.setrecursionlimit(100000)

def get_tokens(a, b, p):
    p_x, p_y = p
    a_x, a_y = a
    b_x, b_y = b

    best_result = float('inf')

    @cache
    def get_presses(cur_x, cur_y, num_a, num_b):
        nonlocal best_result
        if cur_x > p_x or cur_y > p_y:
            return
        if num_a > 150 or num_b > 150:
            return
        if cur_x == p_x and cur_y == p_y:
            best_result = min(best_result, num_a * 3 + num_b)
            return
        if cur_x <= p_x and cur_y <= p_y:
            if (p_x - cur_x) % a_x == 0 and (p_y - cur_y) % a_y == 0:
                num_a_only = (p_x - cur_x) // a_x
                if (cur_y + num_a_only * a_y) == p_y:
                    best_result = min(best_result, (num_a + num_a_only) * 3 + num_b)
            if (p_x - cur_x) % b_x == 0 and (p_y - cur_y) % b_y == 0:
                num_b_only = (p_y - cur_y) // b_y
                if (cur_x + num_b_only * b_x) == p_x:
                    best_result = min(best_result, num_a * 3 + (num_b + num_b_only))
        get_presses(cur_x + a_x, cur_y + a_y, num_a + 1, num_b)
        get_presses(cur_x + b_x, cur_y + b_y, num_a, num_b + 1)

    get_presses(0, 0, 0, 0)
    return best_result if best_result != float('inf') else 0

def main():
    prizes = [item.strip().split('\n') for item in open('input.txt').read().split('\n\n')]
    ans = 0
    for prize in prizes:
        a_str_x, a_str_y = prize[0].split(': ')[1].split(', ')
        b_str_x, b_str_y = prize[1].split(': ')[1].split(', ')
        p_str_x, p_str_y = prize[2].split(': ')[1].split(', ')
        a = (int(a_str_x[2:]), int(a_str_y[2:]))
        b = (int(b_str_x[2:]), int(b_str_y[2:]))
        p = (int(p_str_x[2:]), int(p_str_y[2:]))
        ans += get_tokens(a, b, p)
    print(ans)

main()