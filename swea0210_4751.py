T = int(input())
for tc in range(1, T+1):
    word = input()
    col = (len(word) * 4) + 1
    dia_list = [['.' for _ in range(col)] for _ in range(5)]

    for i in range(5):
        for j in range(col):
            if i % 4 == 0:
                if j % 4 == 2:
                    dia_list[i][j] = '#'
            elif (i % 4) % 2:
                if j % 2:
                    dia_list[i][j] = '#'
            else:
                if j % 4 == 0:
                    dia_list[i][j] = '#'
                if j % 4 == 2:
                    dia_list[i][j] = word[j//4]

    for line in dia_list:
        print(''.join(line))