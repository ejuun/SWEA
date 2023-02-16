# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# l = len(A)
# cnt = 0
# bit = [0] * l
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#
#     print(f'#{tc} {cnt}')




# U = [1, 2, 3, 4]
# N = len(U)
# bit = [0] * N
# def backtrack(k,n, cur_sum): #k : k번 원소에 대한 결정, n: 최종 판단
#
#     if k == n:  #k : 현재 노드(함수호출) 높이 , n:
#         #하나의 부분집합 생성성
#         S = 0
#         for i in range(n):
#             if bit[i]:
#                 print(U[i], end=' '); S += U[i]
#         print('==>', S, cur_sum)
#     else:
#         # for i in range(2):
#         #     bit[k] = i
#         #     backtrack(k + 1, n)
#
#         #0~k-1번까지 결정한 상태
#         bit[k] = 0 #k 번 원소를 미포함
#         backtrack(k+1, n, cur_sum)
#         bit[k] = 1 #k 번 원소를 포함
#         backtrack(k + 1, n, cur_sum + U[k])
#
# backtrack(0, N, 0)

#순열(중복순열)
# U = [1,2,3]
# N = len(U)
# for i in range(N):
#     for j in range(N):
#         if j == i : continue
#         for k in range(N):
#             if k == i or k == j : continue
#             print(U[i], U[j], U[k])
#재귀로 중복 제거 순열 만들기
#1. 전역변수 활용
#2. used
#
# U = [1, 2, 3]
# N = len(U)
#
# # used = [0] * N #선택된 요소들의 정보
# order = [0] * N #실제 순열을 저장
#
# def perm(k, n, used):
#     if k == n:
#         print(order)
#     else:
#         for i in range(N):
#             if used & (1 << i): continue
#             order[k] = U[i]
#             perm(k+1, n, used | (1 << i))
        # for j in range(N):
        #     if used[j] : continue
        #     used[j] = 1
        #     order[1] = U[j]
        #     for k in range(N):
        #         if used[k]: continue
        #         used[k] = 1
        #         order[2] = U[k]
        #         print(order)
        #         used[k] = 0
        #     used[j] = 0
# perm(0, N, 0)

# U = [1, 2, 3, 4]
# N = len(U)

# for i in range(0, N):
#     U[0], U[i] = U[i], U[0]
#     for j in range(1, N):
#         U[1], U[j] = U[j], U[1]
#         for k in range(2, N):
#             U[2], U[k] = U[k], U[2]
#             print(U)
#             U[2], U[k] = U[k], U[2]
#         U[1], U[j] = U[j], U[1]
#     U[0], U[i] = U[i], U[0]
#
# def perm(k, n):
#     if k == n:
#         print(U)
#     else:
#         for i in range(k, N):
#             U[k], U[i] = U[i], U[k]
#             perm(k+1, n)
#             U[k], U[i] = U[i], U[k]
# perm(0,N)

# arr = [4, 8, 5, 2, 3, 7, 9, 6]
#
# def find_max(s, e):
#     #기저 사례
#     print(s,e)
#     if s == e:
#         return arr[s]
#     #일반 사례
#     else:
#         mid = (s+e) // 2
#         a = find_max(s, mid)
#         b = find_max(mid+1, e)
#         return a if a > b else b
#
# print(find_max(0, len(arr)- 1))

