for tc in range(1, int(input())+1):
    num = list(map(int, input().split()))
    check1 = []
    check2 = []

    for i in range(10):
        check1.append([i, 0])
        check2.append([i, 0])

    winner = 0

    for i in range(len(num)):
        if i % 2:
            check2[num[i]][1] += 1
        else:
            check1[num[i]][1] += 1

        if i >= 4:
            for j in range(10):
                if check1[j][1] == 3:
                    winner = 1
                elif check2[j][1] == 3:
                    winner = 2

                if winner:
                    break
            if winner:
                break

            for j in range(8):
                if check1[j][1] != 0 and check1[j+1][1] != 0 and check1[j+2][1] != 0:
                    winner = 1
                elif check2[j][1] != 0 and check2[j+1][1] != 0 and check2[j+2][1] != 0:
                    winner = 2

                if winner:
                    break
            if winner:
                break

    print(f'#{tc} {winner}')