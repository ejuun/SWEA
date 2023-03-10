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


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     m = [list(map(int, input().split()))for _ in range(N)]
#
#     col = [i for i in range(N)]
#     #col[0] ==> 0번행의 열의 위치
#     #col[1] ==> 1번행의 열의 위치
#
#     def perm(k, n, cur_sum):
#         global ans
#
#         if k == n:
#              s = 0
#              for i in range(n):
#                  s += m[i][col[i]]
#                  print(m[i][col[i]], end=' ')
#              print('==>', s, cur_sum)
#              if ans > s:
#                  ans = s
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
    m = [list(map(int, input().split())) for _ in range(N)]

    #순열에 사용할 열 생성
    col = [i for i in range(N)]
    #초기 최솟값, 정답값 생성
    min_val = 101

    def find(i, n, cur_sum):
        global min_val
        global col

        #만약 중간이라도 합산 값이 최솟값 보다 클 경우 종료
        if cur_sum > min_val:
            return

        if i == n:
            s = 0
            for j in range(n):
                s += m[j][col[j]]
                print(j, col[j], end=' ')
            print()
            if min_val > s:
                min_val = s
                return

        else:
            for j in range(i, n):
                col[i], col[j] = col[j], col[i]
                find(i+1, n, cur_sum + m[i][col[i]])
                col[i], col[j] = col[j], col[i]

    find(0, N, 0)

    print(f'#{tc} {min_val}')
