# for tc in range(1, int(input())+1):
#
#     word = [list(map(str, input())) for _ in range(5)]
#
#     max_len = 0
#     for w in word:
#         if max_len < len(w):
#             max_len = len(w)
#
#     for w in word:
#         if len(w) != max_len:
#             while len(w) != max_len:
#                 w.append('*')
#
#     ans = ''
#     for j in range(max_len):
#         for i in range(5):
#             if word[i][j] == '*':
#                 pass
#             else:
#                 ans += word[i][j]
#
#     print(f'#{tc} {ans}')

#sol
# for tc in range(1, int(input()) +1):
#     arr = [input() for _ in range(5)]
#     ans = ''
#
#     for j in range(15):
#         for i in range(5):
#             if j < len(arr[i]):
#                 ans += arr[i][j]
#
#     print(f'{tc} {ans}')
#sol 2
for tc in range(1, int(input()) +1):
    arr = [input() for _ in range(5)]
    ans = ''

    for j in range(15):
        for i in range(5):
            # if j < len(arr[i]):
            try:
                ans += arr[i][j]
            except:
                pass
    print(f'#{tc} {ans}')