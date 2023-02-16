T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    seq = list(map(int, input().split()))

    key = K
    cnt = 0
    bit = [0] * N

    def hap(i, k, s, key):
        global cnt

        if s > key:
            return

        if i == k:
            s = 0
            for j in range(k):
                if bit[j]:
                    s += seq[j]
            if s == key:
                cnt += 1

        else:
            bit[i] = 0
            hap(i + 1, k, s, key)
            bit[i] = 1
            hap(i + 1, k, s+seq[i], key)

    hap(0, N, 0, key)

    print(f'#{tc} {cnt}')
