import sys
sys.stdin = open('sample_input.txt')

T = int(input())

if 1 <= T <= 50:
    for a in range(1, T+1):
        N = int(input())
        card_nums = input()

        counts = [0] * 10
        max_count = 0
        count = []

        if 5 <= N <= 100:

            for i in range(N):
                counts[int(card_nums[i])] += 1

            for j in range(10):
                if max_count <= counts[j]:
                    max_count = counts[j]
                    count = j

            print(f'#{a} {count} {max_count}')