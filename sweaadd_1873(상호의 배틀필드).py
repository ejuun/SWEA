for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    f = [list(map(str, input())) for _ in range(H)]
    N = int(input())
    move = list(map(str, input()))

    def start_pt():
        for i in range(H):
            for j in range(W):
                if f[i][j] == '<' or f[i][j] == '>' or f[i][j] == '^' or f[i][j] == 'v':
                    r, c = i, j
                    return r, c

    r, c = start_pt()

    def S():
        if f[r][c] == '^':
            k = 1
            while r - k >= 0:
                if f[r-k][c] == '#':
                    break
                elif f[r-k][c] == '*':
                    f[r-k][c] = '.'
                    break
                else:
                    k += 1

        elif f[r][c] == 'v':
            k = 1
            while r + k < H:
                if f[r + k][c] == '#':
                    break
                elif f[r + k][c] == '*':
                    f[r + k][c] = '.'
                    break
                else:
                    k += 1

        elif f[r][c] == '<':
            k = 1
            while c - k >= 0:
                if f[r][c - k] == '#':
                    break
                elif f[r][c - k] == '*':
                    f[r][c - k] = '.'
                    break
                else:
                    k += 1

        elif f[r][c] == '>':
            k = 1
            while c + k < W:
                if f[r][c + k] == '#':
                    break
                elif f[r][c + k] == '*':
                    f[r][c + k] = '.'
                    break
                else:
                    k += 1
        return f

    def U():
        if r - 1 >= 0:
            if f[r-1][c] == '.':
                f[r][c] = '^'
                f[r-1][c] = f[r][c]
                f[r][c] = '.'
            else:
                f[r][c] = '^'
        else:
            f[r][c] = '^'

        return f

    def D():
        if r + 1 < H:
            if f[r + 1][c] == '.':
                f[r][c] = 'v'
                f[r + 1][c] = f[r][c]
                f[r][c] = '.'
            else:
                f[r][c] = 'v'
        else:
            f[r][c] = 'v'

        return f

    def L():
        if c - 1 >= 0:
            if f[r][c - 1] == '.':
                f[r][c] = '<'
                f[r][c - 1] = f[r][c]
                f[r][c] = '.'
            else:
                f[r][c] = '<'
        else:
            f[r][c] = '<'

        return f

    def R():
        if c + 1 < W:
            if f[r][c + 1] == '.':
                f[r][c] = '>'
                f[r][c + 1] = f[r][c]
                f[r][c] = '.'
            else:
                f[r][c] = '>'
        else:
            f[r][c] = '>'

        return f

    for m in move:
        if m == 'S':
            S()
        elif m == 'U':
            U()
        elif m == 'D':
            D()
        elif m == 'L':
            L()
        elif m == 'R':
            R()
        r, c = start_pt()

    print(f'#{tc}', end=' ')
    for line in f:
        print(''.join(line))