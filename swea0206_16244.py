T = int(input())
for tc in range(1, T+1):
    case = [[0 for _ in range(10)]for _ in range(10)]

    r, c, N = map(int, input().split())

    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1:
                case[r+i][c+j] = 1
            else:
                if j == 0 or j == N-1:
                    case[r+i][c+j] = 1
    print(f'#{tc}')
    for i in range(10):
        print(*case[i])