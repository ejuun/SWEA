T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    st = list(map(int, input().split()))

    st.insert(0, 0)
    st.append(N)

    i = 0
    cnt = 0
    while i <= st.index(st[-3]):
        if st[i+1] - st[i] > K:
            cnt = 0
            break

        if st[i+2] - st[i] <= K:
            j = 2
            while st[i + j] - st[i] <= K:
                j += 1
                if i + j >= len(st)-1:
                    break
            if j == 2:
                i += j
            else:
                i += (j - 1)
            if i == len(st)-1:
                break
            cnt += 1
        else:
            cnt += 1
            i += 1
    print(f'#{tc} {cnt}')


