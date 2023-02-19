T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    m = [[0] *(N+2) for _ in range(N+2)]
    n = N //2
    white = 0
    black = 0

    m[n][n] = m[n+1][n+1] = 2
    m[n][n+1] = m[n+1][n] = 1


    for _ in range(M):
        x, y, dol = map(int, input().split())
        m[x][y] = dol

        #8방향 처리
        for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        #해당 방향으로 뻗어 나가면서 처리
            tlist = []
            for mul in range(1, N):
                nx, ny = x + dx * mul, y + dy * mul
                #범위 밖 벗어나거나 빈칸일경우
                if m[nx][ny] == 0:
                    break
                #다른 돌일 경우 뒤집기 후보 추가
                elif m[nx][ny] != dol:
                    tlist.append((nx, ny))
                #같은 돌이면 후보들을 모두 뒤집고 종료
                else:
                    while tlist:
                        ti, tj = tlist.pop()
                        m[ti][tj] = dol
                    break
    for line in m:
        black += line.count(1)
        white += line.count(2)

    print(f'#{tc} {black} {white}')