T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    number = list(map(int,input().split()))
    #연속된 M 개의 숫자 합들 저장
    sum_list= []
    for i in range(N-M+1):
        sum_number = 0
        for j in range(M):
            sum_number += number[i+j]
        sum_list.append(sum_number)
    #연속된 M개의 숫자 합들 가장 큰 값과 가장 작은 값 구하기
    max_hap = sum_list[0]
    for num in sum_list:
        if max_hap < num:
            max_hap = num
    min_hap = sum_list[0]
    for num in sum_list:
        if min_hap > num:
            min_hap = num
    print(f'#{tc} {max_hap-min_hap}')