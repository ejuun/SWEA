T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    def Countingsort(num_list, sort_list, max_val):
        count_list = [0] * (max_val + 1)

        for i in range(len(num_list)):
            count_list[num_list[i]] += 1

        for i in range(1, len(count_list)):
            count_list[i] += count_list[i-1]

        for i in range(len(sort_list)-1, -1, -1):
            count_list[num_list[i]] -= 1
            sort_list[count_list[num_list[i]]] = num_list[i]

        return sort_list

    max_val = 0
    for i in num_list:
        if max_val < i:
            max_val = i

    sort_list = [0] * len(num_list)

    s_list = Countingsort(num_list, sort_list, max_val)

    cnt = 1
    for i in range(len(s_list)-1):
        if cnt == K:
            print(f'#{tc} {s_list[i]}')
            break

        if s_list[i+1] != s_list[i]:
            cnt += 1
    else:
        print(f'#{tc} {s_list[-1]}')


