import sys
sys.stdin = open('input.txt')

T = int(input())
if T <= 50:
    for index in range(1, T+1):
        N = int(input())
        nums = list(map(int, input().split()))

        Max = nums[0]
        Min = nums[0]

        for num in nums:
            if num > Max:
                Max = num
            if num < Min:
                Min = num

        res = Max - Min
        print(f'#{index} {res}')