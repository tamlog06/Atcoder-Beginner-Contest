#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache

import platform
if platform.python_implementation() == 'PyPy':
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')


# def solve(S: str) -> int:
def solve(S):
    for i in range(len(S)):
        if ord('A') <= ord(S[i]) <= ord('Z'):
            return i+1


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
