def pos(row,col):
    return 20*row + col

def read_matrix(file_path):
    return [int(x) for x in open(file_path, 'r').read().replace('\n',' ').split(' ')]

def solve(m):
    verticals, horizontals, left_diagonals, right_diagonals = [],[],[],[]

    for row in xrange(0,17):
        for col in xrange(0,20):
            verticals.append([m[pos(row,col)] * m[pos(row+1,col)] * m[pos(row+2,col)] * m[pos(row+3,col)]])

    for row in xrange(0,20):
        for col in xrange(0,17):
            horizontals.append([m[pos(row,col)] * m[pos(row,col+1)] * m[pos(row,col+2)] * m[pos(row,col+3)]])

    for row in xrange(0,17):
        for col in xrange(0,17):
            left_diagonals.append([m[pos(row,col)] * m[pos(row+1,col+1)] * m[pos(row+2,col+2)] * m[pos(row+3,col+3)]])

    for row in xrange(0,17):
        for col in xrange(3,20):
            right_diagonals.append([m[pos(row,col)] * m[pos(row+1,col-1)] * m[pos(row+2,col-2)] * m[pos(row+3,col-3)]])

    maxes = [max(verticals), max(horizontals), max(left_diagonals), max(right_diagonals)]
    return max(maxes)

def main():
    matrix = read_matrix('input')
    print solve(matrix)

if __name__ == '__main__':
    main()