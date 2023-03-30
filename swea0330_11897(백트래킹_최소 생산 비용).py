def perm(i, k, hap):
    global val

    if val <= hap:
        return

    if i == k:
        if val > hap:
            val = hap
            return
        return

    else:
        for j in range(i, k):
            arr[i], arr[j] = arr[j], arr[i]
            perm(i + 1, k, hap + p[i][arr[i]])
            arr[i], arr[j] = arr[j], arr[i]


for tc in range(1, int(input()) + 1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    val = 2000
    arr = [x for x in range(N)]

    perm(0, N, 0)

    print(f'#{tc} {val}')