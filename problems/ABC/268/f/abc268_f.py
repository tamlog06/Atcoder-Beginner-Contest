#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
from functools import lru_cache


# def solve(N: int, S: List[str]) -> int:
def solve(N, S):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = input()
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()
