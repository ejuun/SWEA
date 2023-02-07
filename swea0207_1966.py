T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    #선택 정렬
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if num_list[minIdx] > num_list[j]:
                minIdx = j
        num_list[i], num_list[minIdx] = num_list[minIdx], num_list[i]

    print(f'#{tc}', end=' ')
    print(*num_list)
