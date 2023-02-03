T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data_list = [0] * N
    count_list = [0] * 10
    sort_list = [0] * N
    number = int(input())
    string_number = str(number)
    for num in string_number:
        count_list[int(num)] += 1

    max_count = count_list[-1]
    max_idx = len(count_list)-1
    for i in range(len(count_list)-1, -1, -1):
        if max_count < count_list[i]:
            max_count = count_list[i]
            max_idx = i
    print(f'#{tc} {max_idx} {max_count}')

