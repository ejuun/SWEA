# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     m = [list(map(int, input().split()))for _ in range(N)]
#
#     # sum_val = []
#     # for i in range(1): # 행
#     #     for j in range(N): #열 (0,1,2)
#     #         sum_v = 0
#     #         sum_v += m[i][j]
#     #         for k in range(N): #(0,1) (0,2) (1,2)
#     #             if k == j: continue
#     #             sum_v += m[i+1][k]
#     #             # print(m[i+1][k])
#     #             for l in range(N): #(2, 1, 0)
#     #                 if l == j or l == k : continue
#     #                 sum_v += m[i+2][l]
#     #                 print(m[i+2][l])
#     #                 sum_val.append(sum_v)
#     # print(sum_val)
#     col = [i for i in range(N)]
#     #col[0] ==> 0번행의 열의 위치
#     #col[1] ==> 1번행의 열의 위치
#
#     def perm(k, n, cur_sum):
#         global ans
#
#         if ans <= cur_sum:
#             return
#
#         if k == n:
#             ans = cur_sum
#             # s = 0
#             # for i in range(n):
#             #     s += m[i][col[i]]
#             #     print(m[i][col[i]], end=' ')
#             # print('==>', s, cur_sum)
#             # if ans > s:
#             #     ans = s
#         else:
#             for i in range(k, N):
#                 col[k], col[i] = col[i], col[k]
#                 perm(k+1, n, cur_sum + m[k][col[k]])
#                 col[k], col[i] = col[i], col[k]
#
#     ans = 0xffffff
#     perm(0, N, 0)
#     print(ans)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m = [list(map(int, input().split()))for _ in range(N)]

    col = [i for i in range(N)]
    #col[0] ==> 0번행의 열의 위치
    #col[1] ==> 1번행의 열의 위치

    def perm(k, n, cur_sum):
        global ans

        if k == n:
             s = 0
             for i in range(n):
                 s += m[i][col[i]]
                 print(m[i][col[i]], end=' ')
             print('==>', s, cur_sum)
             if ans > s:
                 ans = s
        else:
            for i in range(k, N):
                col[k], col[i] = col[i], col[k]
                perm(k+1, n, cur_sum + m[k][col[k]])
                col[k], col[i] = col[i], col[k]

    ans = 0xffffff
    perm(0, N, 0)
    print(ans)