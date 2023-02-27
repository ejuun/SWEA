T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    code = [list(map(int, input())) for _ in range(N)]

    cypher = {
        0: [0, 0, 0, 1, 1, 0, 1],
        1: [0, 0, 1, 1, 0, 0, 1],
        2: [0, 0, 1, 0, 0, 1, 1],
        3: [0, 1, 1, 1, 1, 0, 1],
        4: [0, 1, 0, 0, 0, 1, 1],
        5: [0, 1, 1, 0, 0, 0, 1],
        6: [0, 1, 0, 1, 1, 1, 1],
        7: [0, 1, 1, 1, 0, 1, 1],
        8: [0, 1, 1, 0, 1, 1, 1],
        9: [0, 0, 0, 1, 0, 1, 1]
    }

    #시작 지점 구하기
    s_row = 0
    for i in range(N):
        for j in range(M):
            if code[i][j] == 1:
                s_row = i
                break
        if s_row:
            break

    e_col = 0
    for i in range(M-1, 0, -1):
        if code[s_row][i] == 1:
            e_col = i
            break

      #암호코드 변환
    ans_code = []

    for i in range(e_col-55, e_col+1, 7):
        for ky, val in cypher.items():
            if code[s_row][i:i+7] == val:
                ans_code.append(ky)

    # 암호 코드의 참 / 거짓 확인
    check = 0
    #코드변환값의 총합
    ans = 0
    for i in range(len(ans_code)):
        #홀수 인덱스(짝수자리)
        if i % 2:
            check += ans_code[i]
        #짝수 인덱스(홀수자리)
        else:
            check += 3 * ans_code[i]

        ans += ans_code[i]

    #10의 배수인지 확인
    if check % 10 == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} 0')
