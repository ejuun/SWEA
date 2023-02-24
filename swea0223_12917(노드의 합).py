# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#
#     G = [0] * (N+1)
#
#     for _ in range(M):
#         node, value = map(int, input().split())
#         G[node] = value
#
#     def postorder(v):
#         if v > N:
#             return
#         postorder(v*2)
#         postorder(v*2+1)
#         if not G[v]:
#             if v * 2 + 1 <= N:
#                 G[v] = G[v*2] + G[v*2+1]
#             else:
#                 G[v] = G[v*2]
#     postorder(1)
#
#     print(f'#{tc} {G[L]}')

# T = int(input())
# for tc in range(1, T + 1):
#     N, M, L = map(int, input().split())
#
#     tree = [0] * (N + 1)
#
#     for _ in range(M):
#         idx, val = map(int, input().split())
#         tree[idx] = val
#
#     for i in range(N - M, 0, -1):
#         tree[i] = tree[i * 2]
#         if i * 2 + 1 <= N:
#             tree[i] += tree[i * 2 + 1]
#
#     print(tree[L])

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    result = [0] * (N + 1)

    for _ in range(M):
        node, num = map(int, input().split())
        result[node] = num

    def dfs(v):
        if v * 2 > N and v * 2 + 1 > N: #자식이 없는 노드
            return result[v]

        if v * 2 <= N:
            l = dfs(v * 2)
        if v * 2 + 1 <= N:
            r = dfs(v * 2 + 1)

        result[v] = l + r
        return result[v]

    dfs(1)

    print(f'{tc} {result[L]}')