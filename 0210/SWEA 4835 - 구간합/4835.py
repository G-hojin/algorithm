import sys
sys.stdin = open('sample_input.txt')

T = int(input())

if T <= 50:
    for a in range(1, T+1):
        N, M = map(int, input().split())
        nums = list(map(int, input().split()))

        if 10 <= N <= 100 and 2 <= M < N:
            max_num = 0
            min_num = 9999999999
            res = 0

            for i in range(N-M+1):
                sum_num = 0
                for j in range(M):
                    sum_num += nums[i+j]

                if sum_num > max_num:
                    max_num = sum_num

                if sum_num < min_num:
                    min_num = sum_num

            res = max_num - min_num
            print(f'#{a} {res}')


            # for i in range(M):
            #     num_sum += i
            # min_sum = num_sum
            # max_sum = num_sum
            #
            # for i in range(1, N-M+1):
            #
            #     num_sum = num_sum - num_list[]