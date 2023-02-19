T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sco = [list(map(int, input().split())) for _ in range(N)]

    #조합 구하기
    num = list(range(1, N+1))
    com_l = []
    for i in range(1 << len(num)):
        com = []
        for j in range(N):
            if i & (1 << j):
                com.append(num[j])
        com_l.append(com)
    com_l.sort(key= lambda x: len(x))
    ans = []
    for i in range(len(com_l)):
        if len(com_l[i]) == N // 2:
            ans.append(com_l[i])

    #최솟값 구하기
    min_val = 100000000
    #ans길이의 반만큼
    for i in range(len(ans)//2):
        A = B = 0
        for j in range(N // 2):
            for k in range(N//2):
                if k == j:
                    continue
                A += sco[ans[i][j]-1][ans[i][k]-1]
                      # + sco[ans[i][k]-1][ans[i][j]-1])
                B += sco[ans[len(ans)-1-i][j]-1][ans[len(ans)-1-i][k]-1]
                      # + sco[ans[len(ans)-1-i][k]-1][ans[len(ans)-1-i][j]-1])
        val = abs(A-B)
        if min_val > val:
            min_val = val
    print(f'#{tc} {min_val}')








# a = [(1, 3, 5), (2, 4, 5), (7, 8, 9)]
# for i in range(len(a)):
#     for j in range(len(a)):
#         print(a[i][j], a[j])
#         if a[i][j] in a[j]:
#             print('True')
#         else:
#             print('False')

    # sij = []
    # for i in range(N):
    #     for j in range(i+1, N):
    #        sij.append([i, j])

    # new_list = []
    # for k in range(len(sij)):
    #     for i in range(len(sij)):
    #         for j in range(i + 1, len(sij)):
    #             if sij[i][0] != sij[i][1] != sij[j][0] != sij[j][1]:
    #                 new_list.append()
    #
    # min_val = 100000
    # food_sum = 0
    # for i in range(len(sij)):
    #     for j in range(i+1, len(sij)):
    #         if sij[i][0] != sij[i][1] != sij[j][0] != sij[j][1]:
    #             food_sum = abs((sco[sij[i][0]][sij[i][1]] + sco[sij[i][1]][sij[i][0]]) - (sco[sij[j][0]][sij[j][1]] + sco[sij[j][1]][sij[j][0]]))
    #             print(food_sum)
    #         if min_val > food_sum:
    #             min_val = food_sum
    # print(f'#{tc} {min_val}')


