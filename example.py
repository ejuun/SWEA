p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

n, m = len(t), len(p)
i = j = 0

while i < n:
    #일치하지 않으면
    if t[i] != p[j]:
        # i = 1칸 이동 (
        i = i - j
        # j = 0으로 초기화
        j = -1
    i, j = i + 1, j + 1
    #일치하는 경우
    if j == m:
        print(i - m, t[i - m: i])
        j = 0

