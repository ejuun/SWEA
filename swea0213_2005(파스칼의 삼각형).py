# def fac(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fac(n-1)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     print(f'#{tc}')
#     print(1)
#     for i in range(1, N):
#         print(1, end= ' ')
#         for j in range(1, i+1):
#             print(int(fac(i)/(fac(j)*fac(i-j))), end=' ')
#         print()

def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n-1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(int(fac(i)/(fac(j)*fac(i-j))), end=' ')
        print()