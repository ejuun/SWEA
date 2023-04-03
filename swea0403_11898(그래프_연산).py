from collections import deque

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())

    visited = [0] * 1000001

    queue = deque()
    queue.append(N)
    visited[N] = 1

    while queue:
        num = queue.popleft()

        if num == M:
            break

        cals = [1, -1, num, -10]

        for dir in range(4):
            new = num + cals[dir]
            if 1 <= new <= 1000000 and not visited[new]:
                visited[new] = visited[num] + 1
                queue.append(new)

    print(f'#{tc} {visited[M] - 1}')