def bi(low, high, key):
    global r_cnt, l_cnt

    if low > high:
        return -1
    else:
        mid = (low + high) // 2

        if l_cnt > 1 or r_cnt > 1:
            return 0

        if key == A[mid]:
            return 1

        elif key < A[mid]:
            l_cnt += 1
            r_cnt = 0
            return bi(low, mid - 1, key)
        else:
            l_cnt = 0
            r_cnt += 1
            return bi(mid + 1, high, key)


for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(len(B)):
        l_cnt = r_cnt = 0
        if B[i] not in A:
            continue
        if bi(0, a - 1, B[i]):
            ans += 1

    print(f'#{tc} {ans}')