T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    total_list = []

    def spin(num_list):
        spin_list = [[0 for _ in range(N)] for _ in range(N)]
        for a in range(N):
            for b in range(N):
                spin_list[a][b] = num_list[(N - 1) - b][a]

        return spin_list

    s90 = spin(num_list)
    total_list.append(s90)
    s180 = spin(s90)
    total_list.append(s180)
    s270 = spin(s180)
    total_list.append(s270)

    for line in total_list:
        print(line)

    for i in range(N):
        for j in range(3):
            print(total_list[j][i], end=' ')
        print()