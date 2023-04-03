def dfs(i):
    if visited[i]:
        return 0

    visited[i] = 1

    for dot in G[i]:
        if not visited[dot]:
            dfs(dot)
    return 1


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    G = [[] for _ in range(N + 1)]

    for i in range(0, len(lst), 2):
        G[lst[i]].append(lst[i + 1])
        G[lst[i + 1]].append(lst[i])

    visited = [0] * (N + 1)

    ans = 0
    for i in range(1, N + 1):
        ans += dfs(i)

    print(f'#{tc} {ans}')
#############################################
from collections import deque


def bfs(i):
    queue = deque()
    queue.append(i)
    visited[i] = 1

    while queue:
        x = queue.popleft()

        for dot in G[x]:
            if not visited[dot]:
                visited[dot] = 1
                queue.append(dot)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    G = [[] for _ in range(N + 1)]

    for i in range(0, len(lst), 2):
        G[lst[i]].append(lst[i + 1])
        G[lst[i + 1]].append(lst[i])

    visited = [0] * (N + 1)

    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
            cnt += 1

    print(f'#{tc} {cnt}')