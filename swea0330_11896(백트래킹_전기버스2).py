for tc in range(1, int(input()) + 1):
    N, *oil = map(int, input().split())

    i = cnt = 0
    while i < N - 1:
        if i + oil[i] >= N - 1:
            break

        max_dis = dis = 0
        for j in range(i + 1, i + oil[i] + 1):
            if j <= N:
                dis = j + oil[j]
                if max_dis < dis:
                    max_dis = dis
                    a = j
        i = a
        cnt += 1

    print(f'#{tc} {cnt}')