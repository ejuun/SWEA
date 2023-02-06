T = int(input())
for tc in range(1, T+1):
    case = [[0 for _ in range(10)]for _ in range(10)]

    r, c, N = map(int, input().split())
    #정방향
    for i in range(N):
        case[r+i][c+i] = 1

    for i in range(N):
        case[r+N-1-i][c+i] = 1

    print(f'#{tc}')
    for i in range(10):
        print(*case[i])