from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    oil = [list(map(int, input().split())) for _ in range(N)]

    D = [[1e9 for _ in range(N)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    D[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if oil[nx][ny] > oil[x][y]:
                    if D[nx][ny] > D[x][y] + (oil[nx][ny] - oil[x][y]) + 1:
                        D[nx][ny] = D[x][y] + (oil[nx][ny] - oil[x][y]) + 1
                        queue.append((nx, ny))
                else:
                    if D[nx][ny] > D[x][y] + 1:
                        D[nx][ny] = D[x][y] + 1
                        queue.append((nx, ny))

    print(f'#{tc} {D[N - 1][N - 1]}')