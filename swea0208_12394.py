T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    word_list = [list(map(str, input()))for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            line_word = word_list[i][j:M+j]
            #가로 먼저 검사해서 같은 것이 있으면 출력 후 브레이크
            if line_word == line_word[::-1]:
                print(f"#{tc} {''.join(line_word)}")
                break
            #가로에 결과를 만족하는 것이 없으면 line_word 초기화 해서 세로 검사
            line_word = []
            for k in range(j, M+j):
                line_word.append(word_list[k][i])
            if line_word == line_word[::-1]:
                print(f"#{tc} {''.join(line_word)}")
                break