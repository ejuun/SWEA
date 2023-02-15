# for tc in range(1, 11):
#     n, length = map(int, input().split())
#     edge_list = list(map(int, input().split()))
#     G = [[] for _ in range(200)]
#
#     for i in range(0, len(edge_list)-1, 2):
#         G[edge_list[i]].append(edge_list[i+1])
#
#     visited = [0] * 101
#
#     start, end = 0, 99
#
#     visit_list = []
#
#     def dfs(v):
#         visited[v] = 1
#         visit_list.append(v)
#         for w in G[v]:
#             if not visited[w]:
#                 dfs(w)
#
#     dfs(start)
#
#     for vertex in visit_list:
#         if end  == vertex:
#             print(f'#{tc} 1')
#             break
#     else:
#         print(f'#{tc} 0')

# 교수님 풀이
# tc_num ,E = map(int, input().split())
# arr = list(map(int, input().split()))
#
# G = [[] for _ in range(100)] #정점번호 0~99
# #간선 정보를 읽자
# for i in range(0, E*2, 2):
#     u, v = arr[i], arr[i+1] # u -> v
#     G[u].append(v) #유향그래프에 주의
#
# visited = [0] * 100
#
# S = [0]
# visited[0] = 1
# v = 0
# while S: #빈스택이 아닐동안
#     #v의 방문하지 않은 인접 정점 하나 선택
#     for w in G[v]:
#         if not visited[w]:
#             visited[w] = 1
#             S.append(v)
#             v= w
#             break
#         else:
#             v = S.pop()
#
# print(visited[99])
#
# #재귀
# tc_num ,E = map(int, input().split())
# arr = list(map(int, input().split()))
#
# G = [[] for _ in range(100)] #정점번호 0~99
# #간선 정보를 읽자
# for i in range(0, E*2, 2):
#     u, v = arr[i], arr[i+1] # u -> v
#     G[u].append(v) #유향그래프에 주의
#
# visited = [0] * 100
#
# def dfs(v):               #현재 방문할 정점
#     visited[v] = 1
#     if v == 99:
#         return 1
#
#     for w in G[v]:
#         if not visited[w]:
#             if dfs(w):    #1이 반환되면 종료
#                 return 1
#
#     return 0
#
# dfs(0)
#
# print(dfs(0))