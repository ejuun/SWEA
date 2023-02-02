T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    cnt_list = []
    cnt = 1
    for i in range(len(num_list)-1):
        if num_list[i] < num_list[i+1]:
            cnt += 1
            cnt_list.append(cnt)
        else:
            cnt = 1
            cnt_list.append((cnt))
    print(f'#{tc} {max(cnt_list)}')
