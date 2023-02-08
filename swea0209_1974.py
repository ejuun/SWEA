T = int(input())
for tc in range(1, T+1):
    sdocu = [list(map(int, input().split())) for _ in range(9)]

    cnt = 1
    #가로 확인
    #계산 해야되는 행의 갯수
    for i in range(9):
        #1번 : 2~9까지 검사, 2번 : 3~9번
        for j in range(8):
            for k in range(j+1, 9):
                if sdocu[i][j] == sdocu[i][k]:
                    cnt = 0
                    break

    #세로확인
    #계산해야 되는 열의 갯수
    for i in range(9):
        #1번 : 2~9, 2번 : 3~9 ....
        for j in range(8):
            for k in range(j+1, 9):
                if sdocu[j][i] == sdocu[k][i]:
                    cnt = 0
                    break

    #3 x 3 확인
    #검사해야하는 행의 갯수(0,3,6)
    for i in range(3):
        #검사해야하는 열의 갯수(0,3,6)
        for j in range(3):
            #9개의 숫자 확인하는 리스트 생성
            check_list = [0] * 10
            #행에 더하기 (1,4,7 / 2,5,8)
            for k in range(3):
                #열에 더하기 (1,4,7 / 2,5,8)
                for l in range(3):
                    check_list[sdocu[3*i+k][3*j+l]] += 1

            for num in range(1, len(check_list)):
                if check_list[num] != 1:
                    cnt = 0
                    break


    print(f'#{tc} {cnt}')