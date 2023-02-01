def t_b_up(M):
    for i in range(1, M+1):
        print('*' * i)

def t_b_down(M):
    for i in range(M, 0, -1):
        print('*' * i)

def middle(M):
    for i in range(1, M+1):
        print(' ' * (M-i), end='')
        print('*' * (2*i-1), end='')
        print(' ' * (M-i), end='')
        print('')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc}')
    if M == 1:
        t_b_up(N)
    elif M == 2:
        t_b_down(N)
    else:
        middle(N)