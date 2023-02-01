T = int(input())
for tc in range(1,T+1):
    N = int(input())
    number = list(map(int,input().split()))
    
    max_num = number[0]
    for num in number:
        if max_num < num:
            max_num = num
    
    min_num = number[0]
    for num in number:
        if min_num > num:
            min_num = num
    
    print(f'#{tc} {max_num-min_num}')