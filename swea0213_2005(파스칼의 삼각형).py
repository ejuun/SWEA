# def fac(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fac(n-1)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     print(f'#{tc}')
#     for i in range(N):
#         for j in range(i+1):
#             print(int(fac(i)/(fac(j)*fac(i-j))), end=' ')
#         print()



# #재귀
# def comb(n, r):
#     if r == 0 or n == r:
#         return 1
#
#     return comb(n-1, r-1) + comb(n-1, r)
#
# print(comb(10, 2))
#
# #DP
# #메모이제이션
# memo = [[0] * 100 for _ in range(100)]
# def comb(n, r):
#     if r == 0 or n == r:
#         return 1
#
#     if memo[n][r] != 0:
#         return memo[n][r]
#
#     memo[n][r] = comb(n-1, r-1) + comb(n-1, r)
#     return memo[n][r]
#
# print(comb(5, 3))
#
# for line in memo[:6]:
#     print(*line[0:6])

#메모이제이션
memo = [[0] * 100 for _ in range(100)]
def comb(n, r):

    for n in range(N):
        for r in range(n+1):
            if r == 0 or n == r:
                memo[n][r] = 1
            else:
                memo[n][r] = memo[n-1][r-1] + memo[n-1][r]

print(comb(5, 3))

for line in memo[:6]:
    print(*line[0:6])