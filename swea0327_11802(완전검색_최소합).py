for tc in range(1, int(input()) + 1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        num[0][i] += num[0][i - 1]
        num[i][0] += num[i - 1][0]

    for i in range(1, N):
        for j in range(1, N):
            num[i][j] += min(num[i - 1][j], num[i][j - 1])

    print(f'#{tc} {num[N - 1][N - 1]}')