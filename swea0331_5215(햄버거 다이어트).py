for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    dp = [0] * (L + 1)

    for score, kcal in lst:
        for i in range(L, kcal - 1, -1):
            dp[i] = max(dp[i], dp[i - kcal] + score)

    print(f'#{tc} {dp[L]}')