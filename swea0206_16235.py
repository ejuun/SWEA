T = int(input())
for tc in range(1, T+1):
    case = [[0 for _ in range(10)]for _ in range(10)]

    r, c, N = map(int, input().split())
    n = 1
    for i in range(r, r+N):
        for j in range(c, c+N):
            case[i][j] = n
            n += 1

    print(f'#{tc}')
    for i in range(10):
        print(*case[i])