from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    print(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
            if maze[i][j] == 3:
                maze[i][j] = -1
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1] #상하좌우

    maze[r][c] = 0
    result = 0
    queue = deque()
    queue.append((r, c))

    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if not maze[nx][ny]:
                    queue.append((nx, ny))
                    maze[nx][ny] = maze[x][y] + 1
                elif maze[nx][ny] == -1:
                    result = maze[x][y]
                    break
        if result:
            break
    print(f'#{tc} {result}')