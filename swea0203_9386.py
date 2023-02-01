T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    zero_one_str = input()
    cnt_list = []

    i = 0
    j = 1
    while j <= N-1:
        cnt = 0
        if zero_one_str[i] == '1':
            cnt += 1
            while zero_one_str[j] == '1':
                cnt += 1
                j += 1
                if j == N:
                    break
                i = j
            cnt_list.append(cnt)
            i += 1
            j = i + 1
        else:
            i += 1
            j = i + 1
    print(f'#{tc} {max(cnt_list)}')