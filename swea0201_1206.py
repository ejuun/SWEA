for tc in range(1,11):
    N = int(input())
    building = list(map(int,input().split()))
    cnt= 0
    for i in range(2,N-2):
        # left_light = min(building[i] - building[i-1], building[i] - building[i-2])
        # right_light = min(building[i] - building[i+1], building[i] - building[i+2])
        # if left_light > 0  and right_light > 0:
        #     cnt += min(left_light,right_light)
        if building[i] - building[i-1] >= building[i] -building[i-2]:
            left_light = building[i] -building[i-2]
        else: 
            left_light = building[i] -building[i-1]

        if building[i] - building[i+1] >= building[i] -building[i+2]:
            right_light = building[i] -building[i+2]
        else:
            right_light = building[i] -building[i+1]

        if left_light > 0 and right_light > 0:

            if left_light >= right_light:
                cnt += right_light
            else:
                cnt += left_light
    print(f'#{tc} {cnt}')
