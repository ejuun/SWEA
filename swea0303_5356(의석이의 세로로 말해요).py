for tc in range(1, int(input())+1):

    word = [list(map(str, input())) for _ in range(5)]

    max_len = 0
    for w in word:
        if max_len < len(w):
            max_len = len(w)

    for w in word:
        if len(w) != max_len:
            while len(w) != max_len:
                w.append('*')

    ans = ''
    for j in range(max_len):
        for i in range(5):
            if word[i][j] == '*':
                pass
            else:
                ans += word[i][j]

    print(f'#{tc} {ans}')