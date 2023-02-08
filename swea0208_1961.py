T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    def spin(num_list):
        spin_list = [[0 for _ in range(N)] for _ in range(N)]
        for a in range(N):
            for b in range(N):
                spin_list[a][b] = num_list[(N - 1) - b][a]
        return spin_list

    def change_num(s_list):
        h_list =[]
        for i in range(len(s_list)):
            h = ''.join((str(num) for num in s_list[i]))
            h_list.append(h)
        return h_list


    s90 = spin(num_list)
    s180 = spin(s90)
    s270 = spin(s180)
    h90 = change_num(s90)
    h180 = change_num(s180)
    h270 = change_num(s270)

    ans_list = [h90, h180, h270]

    print(f'#{tc}')
    for i in range(N):
        print(ans_list[0][i], ans_list[1][i], ans_list[2][i])
