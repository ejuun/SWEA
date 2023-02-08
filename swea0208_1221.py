word_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

num_list = list(enumerate(word_list))

T = int(input())
for tc in range(1, T+1):
    case_number, length = map(str, input().split())
    words = list(map(str, input().split()))
    change_list = []
    ans_list = []

    for i, w in num_list:
        for word in words:
            if word == w:
                change_list.append(w)

    print(case_number)
    print(*change_list)

    # for j in range(len(change_list)):
    #     for (i, w) in num_list:
    #         if change_list[j] == i:
    #             ans_list.append(w)
    #
    # print(ans_list)

