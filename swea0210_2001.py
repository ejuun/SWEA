T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = [list(map(int,input().split()))for _ in range(N)]

    max_sum = 0

    for a in range(N-M+1):
        for b in range(N-M+1):
            M_sum = 0
            for i in range(M):
                for j in range(M):
                    M_sum += num_list[a+i][b+j]
            if max_sum < M_sum:
                max_sum = M_sum

    print(f'#{tc} {max_sum}')
