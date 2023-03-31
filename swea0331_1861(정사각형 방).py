from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1

    while queue:

        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n:
                if lst[nx][ny] - lst[x][y] == 1:
                    queue.append((nx, ny))
                    cnt += 1
    return cnt


for tc in range(1, int(input()) + 1):
    n = int(input())

    lst = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_cnt = 0

    able = []
    for i in range(n):
        for j in range(n):
            move = bfs(i, j)
            if max_cnt <= move:
                max_cnt = move
                able.append([move, lst[i][j]])

    able.sort(key=lambda x: (-x[0], x[1]))

    print(f'#{tc} {able[0][1]} {able[0][0]}')