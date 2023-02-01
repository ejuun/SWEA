# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     number = list(map(int,input().split()))

#     sum_num_list = []
#     for i in range(N-1):
#         sum_number = 0
#         for j in range(2):
#             sum_number += number[i+j]
#         sum_num_list.append(sum_number)
    
#     max_num = sum_num_list[0]
#     for i in range(1,len(sum_num_list)):
#         if max_num < sum_num_list[i]:
#             max_num = sum_num_list[i]
    
#     print(f'#{tc} {max_num}')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    number = list(map(int,input().split()))
    
    max_num = -400
    for i in range(len(number)-1):
        if max_num < number[i] + number[i+1]:
            max_num = number[i] + number[i+1]
    print(f'#{tc} {max_num}')