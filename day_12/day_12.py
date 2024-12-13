import sys

f = [list(line.strip('\n')) for line in open('input.txt', 'r').readlines()]
ff = [[str(0) for i in range(len(f)+2)] for j in range(len(f)+2)]

def search(letter, matrix):
    perimeter = 0
    patterns = {
        [[0,0],
         [0,1]],
        [[0,0],
         [1,0]]
    }
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == letter:
                letters = 0
                for vec in vecs:
                    check = matrix[i+vec[0]][j+vec[1]]
                    if check == letter:
                        letters += 1
                if letters == 1 or letters == 3:
                    perimeter += 1
    print(perimeter)

for i in range(len(ff)):
    for j in range(len(ff[i])):
        if 0 <= i < len(f) and 0 <= j < len(f[i]):
            if f[i][j] != '0':
                ff[i+1][j+1] = f[i][j]
    print(f'{i} {ff[i]}')


search('A', ff.copy())