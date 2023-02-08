T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    word_dict = {}
    #중복 글자 제거
    for alphabet in str1:
        if alphabet not in word_dict:
            word_dict[alphabet] =0

    #str2에 str1에 포함된 글자를이 몇 개 있는지 확인
    for alphabet in str2:
        if alphabet in word_dict:
            word_dict[alphabet] += 1

    max_val = -1
    for cnt in word_dict.values():
        if max_val < cnt:
            max_val = cnt

    print(f'#{tc} {max_val}')