for tc in range(1, 2):
    N = int(input())
    words = [list(map(str, input())) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            # 가로 검색
            pal_word = words[i][j:j+N]
            if pal_word == pal_word[::-1]:
                cnt += 1
            #세로검색
            pal_word= []
            for k in range(j, N+j):
                print(words[k][i], end='')
                pal_word.append((words[k][i]))
            print()
            if pal_word == pal_word[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')

# A = [['A', 'B', 'C'],['C', 'D', 'B'],['A', 'C', 'C']]
#
# lst = []
# N = 2
# for i in range(3):
#     for j in range(3-N+1):
#         for k in range(N):
#             print(A[j+k][i])
#             lst.append(A[j+k][i])
#             print(lst)

