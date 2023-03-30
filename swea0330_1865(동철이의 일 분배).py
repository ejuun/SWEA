def perm(i, k, mul):
    global ans

    if mul <= ans:
        return

    if i == k:
        if ans < mul:
            ans = mul
            return
        return

    for j in range(i, k):
        arr[i], arr[j] = arr[j], arr[i]
        perm(i + 1, k, mul * (p[i][arr[i]] / 100))
        arr[i], arr[j] = arr[j], arr[i]


for tc in range(1, int(input()) + 1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]

    arr = [i for i in range(N)]

    ans = 0

    perm(0, N, 1)

    result = ans * 100

    print(f'#{tc} {format(result, ".6f")}')