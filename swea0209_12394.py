T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [list(map(str, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            line_word = words[i][j:M+j]
            if line_word == line_word[::-1]:
                print(f"#{tc} {''.join(line_word)}")
                break
            line_word = []
            for k in range(j, M + j):
                line_word.append(words[k][i])
            if line_word == line_word[::-1]:
                print(f"#{tc} {''.join(line_word)}")
                break