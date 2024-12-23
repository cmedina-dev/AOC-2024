import numpy as np

def get_tokens(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p
    M = np.array([
        [ax, bx],
        [ay, by],
    ])
    P = np.array(
        [px, py]
    ) + 10000000000000
    a,b = np.linalg.solve(M, P).round()
    if [a*ax+b*bx, a*ay+b*by] == [*P]:
        return int(a * 3 + b)
    return 0

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