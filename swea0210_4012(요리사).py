T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sco = [list(map(int, input().split())) for _ in range(N)]

    #조합 구하기
    num = list(range(1, N+1))
    com_l = []
    for i in range(1 << len(num)):
        combi = []
        for j in range(N):
            if i & (1 << j):
                combi.append(num[j])
        com_l.append(combi)
    com_l.sort(key= lambda x: len(x))

    #최솟값 구하기
    min_score = 10000

    for i in range(len(com_l)):

        if len(com_l[i]) == N // 2:
            a = 0
            b = 0
            for j in range(N//2):
                a += sco[com_l[i][j]-1][com_l[i][(N//2)-1-j]-1]
                b += sco[com_l[len(com_l)-1-i][j]-1][com_l[len(com_l)-1-i][(N//2)-1-j]-1]
            # print('a',sco[com_l[i][j]-1][com_l[i][(N//2)-1-j]-1])
            # print('b',sco[com_l[len(com_l)-1-i][j]-1][com_l[len(com_l)-1-i][(N//2)-1-j]-1])
            score = abs(a-b)
            if min_score > score:
                min_score = score

    print(f'#{tc} {min_score}')











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


