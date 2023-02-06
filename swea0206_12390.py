A = [1,2,3,4,5,6,7,8,9,10,11,12]
bit = [0] * 12
subset_list = []
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                for i in range(2):
                                    for j in range(2):
                                        for k in range(2):
                                            for l in range(2):
                                                bit = [a,b,c,d,e,f,g,h,i,j,k,l]
                                                subset_list.append(bit)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0

    lenN_subset = []
    for i in subset_list:
        if i.count(1) == N:
            lenN_subset.append(i)

    for i in range(len(lenN_subset)):

        sum_K = 0
        for j in range(len(A)):
            sum_K += (A[j] * lenN_subset[i][j])
        if sum_K == K:
            # if sum(subset_list[i]) == N:
            cnt += 1

    print(f'#{tc} {cnt}')
