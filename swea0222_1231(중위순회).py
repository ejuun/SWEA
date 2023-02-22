# for tc in range(1, 11):
#     N = int(input())
#     G = [0] * (N + 1)
#     word = []
#     for _ in range(N):
#         case = input().split()
#         word.append(case)
#
#     word_list = [[] for _ in range(N+1)]
#     # graph_list = [[] for _ in range(N+1)]
#     for i in range(len(word)):
#         if len(word[i]) == 2:
#             word_list[i+1].append(word[i][1])
#
#         elif len(word[i]) == 3:
#             word_list[i+1].append(word[i][1])
#             # graph_list[i+1].append(int(word[i][2]))
#         else:
#             word_list[i+1].append(word[i][1])
#             # graph_list[i+1].append(int(word[i][2]))
#             # graph_list[i+1].append(int(word[i][3]))
#
#     def inorder(v):
#         if v > N:
#             return
#
#         inorder(v*2)
#         print(word_list[v][0], end= '')
#         inorder(v*2+1)
#
#     print(f'#{tc}', end= ' ')
#     inorder(1)
#     print()

def inorder(v):
    if v > N:
        return

    inorder(v * 2)
    print(word_list[v][0], end='')
    inorder(v * 2 + 1)

for tc in range(1, 11):
    N = int(input())
    G = [0] * (N + 1)
    word = []
    for _ in range(N):
        case = input().split()
        word.append(case)

    word_list = [[] for _ in range(N+1)]

    for i in range(len(word)):
        word_list[i+1].append(word[i][1])

    print(f'#{tc}', end=' ')
    inorder(1)
    if tc == 10:
        continue
    else:
        print()