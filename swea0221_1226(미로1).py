for tc in range(1, 11):
    tc_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    #길 : 0 , 벽 : 1, 출발점 : 2, 도착점 : 3
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                r, c = i, j
            if maze[i][j] == 3:
                maze[i][j] = -1

    queue = []
    queue.append((r, c))

    maze[r][c] = 0
    result = 0

    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]  # 상하좌우

    while queue:
        x, y = queue.pop(0)

        for dir in range(4):
            nr = x + dr[dir]
            nc = y + dc[dir]
            if 0 <= nr < 16 and 0 <= nc < 16:
                if not maze[nr][nc]:
                    queue.append((nr, nc))
                    maze[nr][nc] = maze[x][y] + 1
                if maze[nr][nc] == -1:
                    result = 1
                    break
        if result:
            break
    print(f'#{tc} {result}')