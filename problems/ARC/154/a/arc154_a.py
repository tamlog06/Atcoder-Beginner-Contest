#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache

MOD = 998244353


# def solve(N: int, A: int, B: int) -> int:
def solve(N, A, B):
    a = list(str(A))
    b = list(str(B))

    for i in range(N):
        # ans += str(min(int(a[i]), int(b[i])))
        if int(a[i]) < int(b[i]):
            a[i], b[i] = b[i], a[i]

    ans = int(''.join(a)) * int(''.join(b))
    return int(ans) % MOD

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    A = int(input())
    B = int(input())
    a = solve(N, A, B)
    print(a)


if __name__ == '__main__':
    main()
