import re
import numpy as np

def part_two():
    with open('input.txt', 'r') as f:
        d = np.array([list(line.strip()) for line in f])
    l_col = 0
    m_col = 1
    r_col = 2
    t_row = 0
    m_row = 1
    b_row = 2
    c = 0
    while b_row < len(d):
        while r_col < len(d[0]):
            x_1 = list([d[t_row][l_col], d[m_row][m_col], d[b_row][r_col]])
            x_2 = list([d[b_row][l_col], d[m_row][m_col], d[t_row][r_col]])
            x_3 = list(reversed(x_1))
            x_4 = list(reversed(x_2))
            s_1 = ''.join(x_1)
            s_2 = ''.join(x_2)
            s_3 = ''.join(x_3)
            s_4 = ''.join(x_4)
            if s_1 == 'SAM' and s_2 == 'SAM': c += 1
            elif s_1 == 'SAM' and s_4 == 'SAM': c += 1
            elif s_2 == 'SAM' and s_3 == 'SAM': c += 1
            elif s_3 == 'SAM' and s_4 == 'SAM': c += 1
            l_col += 1
            m_col += 1
            r_col += 1
        l_col = 0
        m_col = 1
        r_col = 2
        t_row += 1
        m_row += 1
        b_row += 1
    print(c)

part_two()

def part_one():
    with open('input.txt', 'r') as f:
        d = np.array([list(line.strip()) for line in f])
    seqs = list()
    for k in range(len(d[0])):
        diag_v = np.diag(d, k=k)
        diag_h = np.diag(d, k=-k)
        d_ = np.fliplr(d)
        diag_v_ = np.diag(d_, k=k)
        diag_h_ = np.diag(d_, k=-k)
        col = d[:, k]
        if k == 0:
            if len(diag_v) > 3:
                seq = ''.join(diag_v)
                seqs.append(seq)
                seqs.append(seq[::-1])
            if len(diag_v_) > 3:
                seq = ''.join(diag_v_)
                seqs.append(seq)
                seqs.append(seq[::-1])
        else:
            if len(diag_v) > 3:
                seq = ''.join(diag_v)
                seqs.append(seq)
                seqs.append(seq[::-1])
            if len(diag_h) > 3:
                seq = ''.join(diag_h)
                seqs.append(seq)
                seqs.append(seq[::-1])
            if len(diag_v_) > 3:
                seq = ''.join(diag_v_)
                seqs.append(seq)
                seqs.append(seq[::-1])
            if len(diag_h_) > 3:
                seq = ''.join(diag_h_)
                seqs.append(seq)
                seqs.append(seq[::-1])
        if len(col) > 3:
            seq = ''.join(col)
            seqs.append(seq)
            seqs.append(seq[::-1])

    for k in range(len(d)):
        seq = ''.join(d[k])
        seqs.append(seq)
        seqs.append(seq[::-1])

    seqs = np.array(seqs)
    xmas = re.compile('XMAS')
    c = 0
    for seq in seqs:
        l = len(re.findall(xmas, seq))
        if l > 0: c += l
    print(c)