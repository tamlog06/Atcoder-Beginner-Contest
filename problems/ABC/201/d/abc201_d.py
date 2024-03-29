#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
from functools import lru_cache


# def solve(n: int, k: int, a: List[str]) -> str:
def solve(H, W, A):
    dp = [[0] * W for _ in range(H)]
    dp[H-1][W-1] = 0

    c = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if A[h][w] == '+':
                c[h][w] = 1
            else:
                c[h][w] = -1

    for h in range(H-1, -1, -1):
        for w in range(W-1, -1, -1):
            if h == H-1 and w == W-1:
                continue

            if w == W-1:
                dp[h][w] = c[h+1][w] - dp[h+1][w]
            elif h == H-1:
                dp[h][w] = c[h][w+1] - dp[h][w+1]
            else:
                dp[h][w] = max(c[h+1][w] - dp[h+1][w], c[h][w+1] - dp[h][w+1])

    if dp[0][0] > 0:
        return 'Takahashi'
    elif dp[0][0] == 0:
        return 'Draw'
    else:
        return 'Aoki'


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    ans = solve(H, W, A)
    print(ans)


if __name__ == '__main__':
    main()
