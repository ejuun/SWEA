# from collections import deque
#
# def bfs(r, c):
#     dx = [-1, 1, 0, 0]  # 상 하 좌 우
#     dy = [0, 0, -1, 1]
#
#     cnt = 1
#     queue = deque()
#     queue.append((r, c))
#     if visitied[r][c]:
#         return 0
#
#     visitied[r][c] = 1
#
#     while queue:
#         x, y = queue.popleft()
#
#         for dir in range(4):
#             nx = x + dx[dir]
#             ny = y + dy[dir]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if not visitied[nx][ny]:
#                     if abs(room[nx][ny] - room[x][y]) == 1:
#                         queue.append((nx, ny))
#                         visitied[nx][ny] = 1
#                         cnt += 1
#                         if room[nx][ny] < room[x][y]:
#
#     return cnt
#
# T = int(input())
# for tc in range(1, T+1):
#
#     N = int(input())
#     #방 생성
#     room = [list(map(int, input().split())) for _ in range(N)]
#     visitied = [[0 for _ in range(N)] for _ in range(N)]
#
#     max_val = 0
#     start = 1000000
#     for i in range(N):
#         for j in range(N):
#             a = bfs(i, j)
#             if max_val <= a:
#                 max_val = a
#
#
#     print(f'#{tc} {start} {max_val}')
def bfs(si, sj):
    q = []
    alst = []

    q.append((si, sj))
    visitied[si][sj] = 1
    alst.append(room[si][sj])

    while q:
        ci, cj = q.pop(0)

        # 4방향, 미방문, 조건 맞으면! (1차이)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visitied[ni][nj] == 0 and abs(room[ci][cj] - room[ni][nj]) == 1:
                q.append((ni, nj))
                visitied[ni][nj] = 1
                alst.append(room[ni][nj])

    return min(alst), len(alst)


T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visitied = [[0 for _ in range(N)] for _ in range(N)]
    ans, cnt = N * N, 0
    for si in range(N):
        for sj in range(N):
            if visitied[si][sj] == 0:
                t, tcnt = bfs(si, sj)
                if cnt < tcnt or (cnt == tcnt and ans > t):
                    ans, cnt = t, tcnt

    print(f'#{tc} {ans} {cnt}')
