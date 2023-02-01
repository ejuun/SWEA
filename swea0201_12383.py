T = int(input())
for tc in range(1,T+1):
    N = int(input())
    number = list(map(int,input().split()))
    diff_list = []
    for i in range(N-1):
        cnt = 0
        for j in range(i+1,N):
            if number[i] > number[j]:
                cnt += 1
        diff_list.append(cnt)
    max_diff = diff_list[0]        
    for i in range(1,len(diff_list)):
        if max_diff < diff_list[i]:
            max_diff =diff_list[i]

    print(f'#{tc} {max_diff}')