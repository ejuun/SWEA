T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number_list = list(map(int, input().split()))

    max_number = number_list[0]
    max_id = 0
    min_number = number_list[0]
    min_id = 0
    for i in range(len(number_list)):
        if max_number <= number_list[i]:
            max_number = number_list[i]
            max_id = i

    for j in range(len(number_list)):
        if min_number > number_list[j]:
            min_number = number_list[j]
            min_id = j

    print(f'#{tc} {abs(max_id-min_id)}')