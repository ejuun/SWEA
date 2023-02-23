from collections import deque
import copy
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]


    def bfs(r, c):
        dx = [-1, 1, 0, 0] #상 하 좌 우
        dy = [0, 0, -1, 1]

        cnt = 1
        queue = deque()
        queue.append((r, c))

        visited[r][c] = -2

        while queue:
            x, y = queue.popleft()

            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < N and 0 <= ny < N:
                    if abs(room[nx][ny] - room[x][y]) == 1:
                        visited[nx][ny] = -2
                        queue.append((nx, ny))
                        cnt += 1
        return cnt
    max_val =
    for i in range(N):
        for j in range(N):
            visited = copy.deepcopy(room)
            bfs(i,j)
