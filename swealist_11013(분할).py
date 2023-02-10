T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    #0~N-1까지 수 생성
    combi =[]
    for i in range(N):
        combi.append(i)
    #3가지 더해서 N이 되는 경우 구하기
    three =[]
    for i in range(1, len(combi)):
        for j in range(1, len(combi)):
            for k in range(1, len(combi)):
                if i + j + k == N:
                    three.append([i, i+j, i+j+k])

    min_list = []
    for i in range(len(three)):
        hap1 = sum(num[0:three[i][0]])
        hap2 = sum(num[three[i][0]:three[i][1]])
        hap3 = sum(num[three[i][1]:three[i][2]])

        hap_list = [hap1, hap2, hap3]
        max_val = -1000000
        min_val = 1000000
        for j in range(len(hap_list)):
            if max_val < hap_list[j]:
                max_val = hap_list[j]
        for j in range(len(hap_list)):
            if min_val > hap_list[j]:
                min_val = hap_list[j]
        min_list.append(max_val - min_val)

        little_num = 1000000
        for j in range(len(min_list)):
            if little_num > min_list[j]:
                little_num = min_list[j]
    print(f'#{tc} {little_num}')
        # min_list.append(max(hap1, hap2, hap3)-min(hap1, hap2, hap3))
    # print(min(min_list))











