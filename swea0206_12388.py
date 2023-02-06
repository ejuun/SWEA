T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case_list = []
    for i in range(N):
        case = list(map(int, input().split()))
        case_list.append(case)

    red_count = 0
    blue_count = 0
    #빨간색, 파란색 갯수 구하기
    for case in case_list:
        if case[-1] == 1:
            red_count += (case[2] - case[0] + 1) * (case[3] - case[1] + 1)
        elif case[-1] == 2:
            blue_count += (case[2] - case[0] + 1) * (case[3] - case[1] + 1)

    # 빨간색 위치, 파란색 위치
    red_total = []
    blue_total = []
    for case in case_list:
        if case[-1] == 1:
            for i in range(case[0], case[2]+1):
                for j in range(case[1], case[3]+1):
                        red_total.append((i, j))
        elif case[-1] == 2:
            for i in range(case[0], case[2]+1):
                for j in range(case[1], case[3]+1):
                        blue_total.append((i, j))

    red = list(set(red_total))
    blue = list(set(blue_total))
    purple_count = 0

    for i in red:
        if i in blue:
            purple_count += 1

    print(f'#{tc} {purple_count}')
