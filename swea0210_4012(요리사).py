T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sco = [list(map(int, input().split())) for _ in range(N)]

    #조합 구하기
    num = []
    re_num = []
    for i in range(N//2):
        num.append(i)
        re_num.append((N//2)+i)
    print(num, re_num)













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


