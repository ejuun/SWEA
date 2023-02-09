for tc in range(1, 2):
    tc_num = int(input())
    pal_list = [list(map(str, input())) for _ in range(100)]

    N = 100
    max_length = 1
    while N > 2:
        for i in range(100):
            for j in range(100 - N + 1):
                #가로
                pal_word = pal_list[i][j:j+N]
                if pal_word == pal_word[::-1]:
                    if max_length < len(pal_word):
                        max_length = len(pal_word)
                #세로
                pal_word = []
                for k in range(j, N+j):
                    pal_word.append(pal_list[k][i])
                if pal_word == pal_word[::-1]:
                    if max_length < len(pal_word):
                        max_length = len(pal_word)
        N -= 1
        if max_length != 1:
            break
    print(f'#{tc} {max_length}')

