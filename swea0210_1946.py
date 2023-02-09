T = int(input())
for tc in range(1, T+1):
    N = int(input())

    word_list = []
    for n in range(N):
        word, num = map(str, input().split())
        for i in range(int(num)):
            word_list.append(word)

    remainder = len(word_list) % 10
    share = len(word_list) // 10

    print(f'#{tc}')
    if share == 0:
        for i in range(remainder):
            print(word_list)
    else:
        for i in range(share):
            print(''.join(word_list[i*10:(i+1)*10]))
        for i in range(share*10):
            word_list.pop(0)
        print(''.join(word_list))
