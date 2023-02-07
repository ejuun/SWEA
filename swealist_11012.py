T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    matrix = []
    for n in range(N):
        num_list =list(map(int, input().split()))
        matrix.append((num_list))

    sum_num = 0
    range_list = [] #덧셈하는 배열 위치를 모두 저장
    for m in range(M):
        x, y, size = map(int, input().split())
        for i in range(size):
            for j in range(size):
                range_list.append((x+i, y+j))

    range_set = set(range_list)

    for rnge in range_set:
        try:
            sum_num += matrix[rnge[0]][rnge[1]]
        except Exception:
            pass

    print(f'#{tc} {sum_num}')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     matrix = []
#     for n in range(N):
#         num_list =list(map(int, input().split()))
#         matrix.append((num_list))
#
#     sum_num = 0
#     range_list = [] #덧셈하는 배열 위치를 모두 저장
#
#     for m in range(M):
#         x, y, size = map(int, input().split())
#         for i in range(size):
#             for j in range(size):
#                 range_list.append((x+i, y+j))
#                 # 리스트 범위 벗어나는 값 더할 시 오류 발생 제거
#                 try:
#                     sum_num += matrix[x+i][y+j]
#                 except Exception:
#                     pass
#
#     # 덧셈 완료 후 겹치는 부분 찾아서 해당 인덱스에 위치한 값 빼주기
#     range_dict = {}
#     for rnge in range_list:
#         if rnge in range_dict:
#             range_dict[rnge] += 1
#         else:
#             range_dict[rnge] = 0
#
#     for idx, cnt in range_dict.items():
#         if cnt != 0:
#             sum_num -= (matrix[idx[0]][idx[1]] * cnt)
#
#     print(f'#{tc} {sum_num}')
#
