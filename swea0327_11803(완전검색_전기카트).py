def perm(i, N):
    if i == N:
        # if arr[-1] == 0:
        able.append(arr[:])

    else:
        for j in range(i, N):
            arr[i], arr[j] = arr[j], arr[i]
            perm(i + 1, N)
            arr[i], arr[j] = arr[j], arr[i]


for tc in range(1, int(input()) + 1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    able = []

    arr = [0] * N
    for i in range(N):
        arr[i] = i+1

    perm(0, N-1)

    for abl in able:
        abl[-1] = 0

    min_val = 10000
    for abl in able:

        hap = idx = 0

        for j in range(len(abl)):
            hap += num[idx][abl[j]]
            idx = abl[j]

        if min_val > hap:
            min_val = hap

    print(f'#{tc} {min_val}')