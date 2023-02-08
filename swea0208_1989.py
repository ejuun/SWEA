T = int(input())
for tc in range(1, T+1):
    word = input()

    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            print(f'#{tc} 0')
            break
    else:
        print(f'#{tc} 1')

# T = int(input())
# for tc in range(1, T+1):
#     word = input()
#
#     ans = 1
#     for i in range(len(word)//2):
#         if word[i] != word[-(i+1)]:
#             ans = 0
#             break
#
#     print(f'#{tc} {ans}')