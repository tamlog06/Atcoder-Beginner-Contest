#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
from functools import lru_cache

YES = 'Yes'
NO = 'No'


# def solve(n: int, a: List[int]) -> str:
def solve(A):
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        return YES
    else:
        return NO


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A = list(map(int, input().split()))

    ans = solve(A)
    print(ans)


if __name__ == '__main__':
    main()
