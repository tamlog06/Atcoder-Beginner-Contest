#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
from functools import lru_cache


# def solve(N: int, p: List[int]) -> int:
def solve(N, p):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    p = [None for _ in range(N)]
    for i in range(N):
        p[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, p)
    print(a)


if __name__ == '__main__':
    main()
