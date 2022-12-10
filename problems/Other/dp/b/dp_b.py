#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[int]) -> Any:
def solve(N, K, h):
    dp = [float('inf')] * N
    dp[0] = 0

    for i in range(1, N):
        dp[i] = min(dp[i-j] + abs(h[i] - h[i-j]) for j in range(1, min(K, i)+1))

    return dp[N-1]



# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    print(solve(N, K, h))


if __name__ == '__main__':
    main()
