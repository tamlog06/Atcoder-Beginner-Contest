#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
from functools import lru_cache


# def solve(N: int, P: List[int], A: List[int], B: List[int], C: List[int]) -> int:
def solve(N, P, A, B, C):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    P = [None for _ in range(N)]
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    C = [None for _ in range(N)]
    for i in range(N):
        P[i] = int(next(tokens))
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, P, A, B, C)
    print(a)


if __name__ == '__main__':
    main()
