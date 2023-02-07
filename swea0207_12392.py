T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    #선택 정렬 활용
    def selectionSort(num_list, N):
        #홀수일때 최솟값 넣기
        for i in range(N-1):
            minIdx = i
            maxIdx = i
            if i % 2:
                for j in range(i+1, N):
                    if num_list[minIdx] > num_list[j]:
                        minIdx = j
                num_list[i], num_list[minIdx] = num_list[minIdx], num_list[i]
        #짝수일때 최댓값 넣기
            else:
                for j in range(i+1, N):
                    if num_list[maxIdx] < num_list[j]:
                        maxIdx = j
                num_list[i], num_list[maxIdx] = num_list[maxIdx], num_list[i]

        return num_list

    selectionSort(num_list, N)

    print(f'#{tc}', end=' ')
    if len(num_list) > 10:
        print(*num_list[:10])
    else:
        print(*num_list)


    # sort_list = [0] * len(num_list)
    #
    # max_val = 0
    # for i in num_list:
    #     if max_val < i:
    #         max_val = i
    #
    # #카운팅 정렬 함수 정의
    # def Counting_sort(num_list, sort_list, max_val):
    #     count_list = [0] * (max_val+1)
    #
    #     for i in range(0, len(num_list)):
    #         count_list[num_list[i]] += 1
    #
    #     for i in range(1, len(count_list)):
    #         count_list[i] += count_list[i-1]
    #
    #     for i in range(len(sort_list)-1, -1, -1):
    #         count_list[num_list[i]] -= 1
    #         sort_list[count_list[num_list[i]]] = num_list[i]
    #
    #     return sort_list
    #
    # Counting_sort(num_list, sort_list, max_val)
    #
    # ans_list = [0] * N
    # add = 0
    # even = 0
    # for i in range(N):
    #     #i가 짝수이면 큰수 넣기
    #     if i % 2 == 0:
    #         ans_list[i] = sort_list[-(even+1)]
    #         even += 1
    #         # a[0] a[2] a[4] a[6] a[8] = s[-1] s[-2] s[-3] s[-4] s[-5]
    #     #i가 홀수이면 작은수 넣기
    #     else:
    #         ans_list[i] = sort_list[add]
    #         #a[1] a[3] a[5] a[7] a[9] = s[0] s[1] s[2] s[3] s[4]
    #         add += 1
    #
    # print(f'#{tc}', end=' ')
    # if len(ans_list) > 10:
    #     print(*ans_list[:10])
    # else:
    #     print(*ans_list)

