T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number_list = list(map(int,input().split()))
    count_list = [0] * (max(number_list) + 1)
    for number in number_list:
        count_list[number] += 1

    max_count_number = count_list[0]
    max_idx = 0
    for i in range(len(count_list)):
        if max_count_number <= count_list[i]:
            max_count_number = count_list[i]
            max_idx = i
    print(f'#{tc} {max_idx}')
