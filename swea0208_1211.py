for tc in range(1, 11):
    tc_num = int(input())
    ladders = [list(map(int, input().split()))for _ in range(100)]

    #출발점 위치 구하기
    start_list = []
    for i in range(len(ladders)):
        if ladders[0][i] == 1:
            start_list.append(i)

    def ladder(ladders, r, c):
        cnt = 0
        while r < 99:
            #왼쪽 방향 검사
            if c -1 >= 0 and ladders[r][c-1] == 1:
                #만약 있다면 길이 없을때 까지 왼쪽으로 이동
                while c-1 >= 0 and ladders[r][c-1] == 1:
                    c -= 1
                    cnt += 1
            #오른쪽 방향 검사
            elif c + 1 < 100 and ladders[r][c+1] == 1:
                #만약 있다면 길이 없을 때 까지 오른쪽으로 이동
                while c + 1 < 100 and ladders[r][c+1] == 1:
                    c += 1
                    cnt += 1
                #왼,오른쪽 모두 길이 없다면 아래로 진행
            r += 1
            cnt += 1
        return cnt

    min_count = 999
    min_sp = 0
    for sp in start_list:
        if min_count >= ladder(ladders, 0, sp):
            min_count = ladder(ladders, 0, sp)
            min_sp = sp
    print(f'#{tc} {min_sp}')