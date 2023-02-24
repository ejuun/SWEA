# cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]
#
# def solve_loop():
#     mx = 0
#     for si in range(N):
#         for sj in range(N):  # 가능한 모든 시작위치
#             for k in range(1, 2 * N):
#                 cnt = 0
#                 for i in range(si - k + 1, si + k):
#                     t = abs(si - i)
#                     for j in range(sj - k + 1 + t, sj + k - t):
#                         if 0 <= i < N and 0 <= j < N:
#                             cnt += arr[i][j]  # 집위치를 더하기
#                 #운영비용보다 수익이 같거나 큰 경우 정답 갱신
#                 # if ((k*k)+(k-1)*(k-1)) <= cnt * M:
#                 if cost[k] <= cnt * M:
#                     mx = max(mx, cnt)
#     return mx

cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]

def bfs(si, sj):
    q = []
    v = [[0] for _ in range(N)]
    old = 0
    mx = 0

    q.append((si, sj))
    v[si][sj] = 1
    cnt = arr[si][sj]  # 시작좌표 집이면 1, 아니면 0

    while q:
        ci, cj = q.pop(0)

        if old != v[ci][cj]: #k 값이 달라진 경우
            old = v[ci][cj]
            if cost[v[ci][cj]] <= cnt * M :
                mx = max(mx, cnt)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += arr[ni][nj]
    return mx

def solve_bfs():
    mx = 0
    for si in range(N):
        for sj in range(N):
            mx = max(mx, bfs(si,sj))

    return mx

home = []
cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]

def solve_idea():
    mx = 0
    for si in range(N):
        for sj in range(N):  # 1. 집의 모든 위치를 저장
            if arr[si][sj] == 1:
                home.append((si, sj))

    # 2. 각 기준 위치에서 거리별 집의 개수 누적
    for si in range(N):
        for sj in range(N):
            dist = [0] * 40
            # 거리별 집 위치를 누적
            for ti, tj in home:
                t = abs(si - ti) + abs(sj - tj) + 1
                dist[t] += 1

            for k in range(1, 40):
                dist[k] += dist[k - 1]
                if cost[k] <= dist[k] * M:
                    mx = max(mx, dist[k])
    return mx

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve_bfs()
    # ans = solve_idea()

    print(f'#{tc} {ans}')
