T = int(input())
for tc in range(1, T+1):
    N = float(input())

    bi = ''
    for i in range(1, 13):
        if N < 2 ** (-i):
            bi = bi + '0'
        else:
            bi = bi + '1'
            N = N - 2 ** (-i)

        if N == 0:
            break

    if N != 0:
        result = 'overflow'
    else:
        result = bi

    print(f'#{tc} {result}')