#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
from functools import lru_cache


# def solve(N: int, K: int, A: List[int]) -> int:
def solve(N, K, A):
    ans = -1
    A = sorted(list(set(A)))
    for i in range(K):
        if i >= len(A) or A[i] != i:
            ans = i
            break

    if ans == -1:
        return A[K-1] + 1
    else:
        return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    a = solve(N, K, A)
    print(a)


if __name__ == '__main__':
    main()
