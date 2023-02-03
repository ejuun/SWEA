for tc in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))

    move = 0
    while move < dump:
        box_list[box_list.index(max(box_list))] -= 1
        box_list[box_list.index(min(box_list))] += 1
        move += 1
        if box_list[box_list.index(max(box_list))] - box_list[box_list.index(min(box_list))] == 0:
            break
    print(f'#{tc} {max(box_list)-min(box_list)}')