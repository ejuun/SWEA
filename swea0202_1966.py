T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 1 4 7 8 0
    number_list = list(map(int, input().split()))
    count_list = [0] * (max(number_list)+1) #최댓값보다 1개 큰 값
    sort_list = [0] * len(number_list)

    for num in number_list:
        count_list[num] += 1
        #count_list = [1, 1, 0, 0, 1, 0, 0, 1, 1]

    for i in range(1, len(count_list)):
        count_list[i] = count_list[i] + count_list[i-1]
        #count_list = [1, 2, 2, 2, 3, 3, 3, 4, 5]

    for i in range(len(sort_list)-1, -1, -1):
        count_list[number_list[i]] -= 1 #인덱스값 맞춰주기 위해
        #number_list 내에 있는 값만 호출 됨
        sort_list[count_list[number_list[i]]] = number_list[i]
        #sort_list 내 알맞는 위치에 해당 number값 넣기
        # [0, 2, 2, 2, 3, 3, 3, 4, 5]
        # [0, 0, 0, 0, 0]
        # [0, 2, 2, 2, 3, 3, 3, 4, 4]
        # [0, 0, 0, 0, 8]
        # [0, 2, 2, 2, 3, 3, 3, 3, 4]
        # [0, 0, 0, 7, 8]
        # [0, 2, 2, 2, 2, 3, 3, 3, 4]
        # [0, 0, 4, 7, 8]
        # [0, 1, 2, 2, 2, 3, 3, 3, 4]
        # [0, 1, 4, 7, 8]

    print(f'#{tc}', end=' ')
    for num in sort_list:
        print(num, end=' ')
    print('')

