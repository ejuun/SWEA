# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# A = [1, 2, 3, 4]
# n = len(A)
# subset = []
# for i in range(1 << n): #부분 집합의 개수
#     sub = []
#     for j in range(n): #원소의 수만큼 비트를 비교함
#         if i & (1 << j): # i의 j번 비트가 1인경우
#             sub.append(A[j])
#     subset.append(sub)
#
# print(subset)

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
A = [1,2,3,4]
S = [[]]

for ele in A:
    for i in range(len(S)):
        S.append(S[i] + [ele])
    print(S)
print(S)