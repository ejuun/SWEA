T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    land = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0, -1, 1, 1, -1] #상 하 좌 우 1시 5시 7시 11시
    dy = [0, 0, -1, 1, 1, 1, -1, -1] #상 하 좌 우 1시 5시 7시 11시

    able = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for dir in range(8):
                nx = i + dx[dir]
                ny = j + dy[dir]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                else:
                    if land[i][j] > land[nx][ny]:
                        cnt += 1
            if cnt >= 4:
                able += 1

    print(f'#{tc} {able}')