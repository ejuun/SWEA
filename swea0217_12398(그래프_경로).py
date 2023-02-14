T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    Graph = [[] for _ in range(V+1)] #인접리스트
    visited = [0] * (V+1) #방문정보(한번 갔던데 다시 가지 않으려고)
                              #cycle 방지
    #dfs 구현시 인접리스트, 스택, 방문정보 저장리스트 필요
    #재귀 호출시 stack은 필요 없음
    for _ in range(E):
        u, v = map(int, input().split())
        Graph[u].append(v)

    visit_list = []

    def dfs(v):
        visited[v] = 1
        visit_list.append(v)
        for w in Graph[v]:
            if not visited[w]:
                dfs(w)

    S, G = map(int, input().split())
    dfs(S)
    for end in visit_list:
        if end == G:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')

# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#
#     G = [[] for _ in range(V+1)] #인접리스트
#     stack = [] #스택(지나온 정점을 저장)
#     visited = [0] * (V+1) #방문정보(한번 갔던데 다시 가지 않으려고)
#                           #cycle 방지
#     #dfs 구현시 인접리스트, 스택, 방문정보 저장리스트 필요
#     #재귀 호출시 stack은 필요 없음
#     for _ in range(E):
#         u, v = map(int, input().split())
#         G[u].append(v)
#         G[v].append(u)
#
#     v = 1
#     visited[1] = 1
#     stack.append(v)
#     while stack: #빈 스택이 아닐동안
#         print(stack)
#         #정점 v에 인접한 정점 중에서 ==> G[v]
#         for w in G[v]:
#         #방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w 방문
#             if not visited[w]:
#                 # v ====> w
#                 stack.append(v)
#                 visited[w] = 1; #print(w,end=' ')
#                 v = w #그리고 w를 v로 하여 다시 반복
#                 break
#         else:
#             v = stack.pop()
#         #방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해 pop 실행