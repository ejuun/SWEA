T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
            if maze[i][j] == 3:
                maze[i][j] = -1

    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]  # 상하좌우

    #출발점 초기화
    maze[r][c] = 0
    queue = []
    queue.append((r, c))

    result = 0
    while queue:
        x, y = queue.pop(0)

        for dir in range(4):
            nx = r + dx[dir]
            ny = c + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if not maze[nx][ny]:
                    queue.append((nx, ny))
                    #방문처리(거리추가)
                    maze[nx][ny] = maze[x][y] +1
                #다음 움직일 점이 도착점에 도달했다면
                if maze[nx][ny] == -1:
                    result = maze[x][y]
                    break
        if result:
            break

    print(f'#{tc} {result}')
