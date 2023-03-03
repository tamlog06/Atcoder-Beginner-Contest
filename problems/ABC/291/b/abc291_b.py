#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache

import platform
if platform.python_implementation() == 'PyPy':
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')


# def solve(N: int, X: List[int]) -> float:
def solve(N, X):
    X.sort()
    ans = 0
    for i in range(N, 4 * N):
        ans += X[i]
    return ans / (3 * N)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = [None for _ in range(5 * N)]
    for i in range(5 * N):
        X[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, X)
    print(a)


if __name__ == '__main__':
    main()
