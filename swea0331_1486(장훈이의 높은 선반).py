for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))

    ans = 0xfffffffffff

    def high(i, hap):
        global ans

        if ans < hap - B:
            return

        if i == N:
            if hap >= B and ans > hap - B:
                ans = hap - B
                return
            return

        else:
            high(i + 1, hap + h[i])
            high(i + 1, hap)


    high(0, 0)
    print(f"#{tc} {ans}")