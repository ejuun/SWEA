T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sco = [list(map(int, input().split())) for _ in range(N)]

    #자료 N개일때 나올수 있는 가짓수 구하기 = (N*(N-1)) // 4

    #나올 수 있는 조합 구하기
    all_combi = []
    for i in range(N):
        for j in range(i+1,N):
            all_combi.append([i,j])
    able_combi =[ ]
    for i in range(len(all_combi)):
        a = all_combi[i][0]
        b = all_combi[i][1]
        for j in range(i+1, len(all_combi)):

















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