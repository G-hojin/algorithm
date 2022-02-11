import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    heights = list(map(int, input().split()))

    #dump 횟수만큼 순환
    for i in range(dump):

        # 최소값과 최대값 구해주기
        min_height = 100
        max_height = 0
        for height in heights[:]:
            if height > max_height:
                max_height = height
            if height < min_height:
                min_height = height

        #최대 높이 값에 1을 빼기
        for j in range(len(heights)):
            if heights[j] == max_height:
                heights[j] -= 1
                break
        # 최소 높이 값에 1을 더하기
        for j in range(len(heights)):
            if heights[j] == min_height:
                heights[j] += 1
                break

        # 최소값과 최대값 구해주기
        min_height = 100
        max_height = 0
        for height in heights[:]:
            if height > max_height:
                max_height = height
            if height < min_height:
                min_height = height

        # 최대높이 최소높이차 비교
        if max_height - min_height <= 1:
            break

    print(f'#{tc} {max_height - min_height}')