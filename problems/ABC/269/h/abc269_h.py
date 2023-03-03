#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache

MOD = 998244353


# def solve(N: int, P: List[int]) -> List[str]:
def solve(N, P):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    P = [None for _ in range(N - 1)]
    for i in range(N - 1):
        P[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, P)
    for i in range(N):
        print(ans[i])


if __name__ == '__main__':
    main()
