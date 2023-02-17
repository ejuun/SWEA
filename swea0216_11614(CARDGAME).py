T = int(input())
for tc in range(1, T+1):
    N = int(input())
    parti = [0] + list(map(int, input().split()))

    def win(start_val, end_val):
        if start_val == end_val:
            return start_val
        elif start_val == 1 and end_val == 3: #가위, 보
            return start_val
        elif start_val == 2 and end_val == 1: #바위, 가위
            return start_val
        elif start_val == 3 and end_val == 2: #보, 바위
            return start_val
        else:
            return end_val

    def winner(start, end):
        if start == end:
            return start
        else:
            mid = (start + end) // 2
            a = winner(start, mid)
            b = winner(mid + 1, end)
            if win(parti[a], parti[b]) == parti[a]:
                return a
            return b

    w = winner(1, N)
    print(f'#{tc} {w}')
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     parti = [0] + list(map(int, input().split()))
#
#     def win(start, end): #값
#         if start == end:
#             return start
#         elif start == 1 and end == 3: #가위, 보
#             return start
#         elif start == 2 and end == 1: #바위, 가위
#             return start
#         elif start == 3 and end == 2: #보, 바위
#             return start
#         else:
#             return end
#
#     def winner(start, end): #인덱스
#         if start == end:
#             return start
#         else:
#             mid = (start + end) // 2
#             a = winner(start, mid)
#             b = winner(mid + 1, end)
#             if win(parti[a], parti[b]) == parti[a]:
#                 return a #인덱스
#             return b #인덱스
#
#     w = winner(1, N)
#     print(f'#{tc} {w}')