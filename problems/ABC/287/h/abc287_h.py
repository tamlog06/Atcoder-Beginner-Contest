#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)


# def solve(N: int, M: int, a: List[int], b: List[int], Q: int, s: List[int], t: List[int]) -> Tuple[int, List[int]]:
def solve(N, M, a, b, Q, s, t):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    a = [None for _ in range(M)]
    b = [None for _ in range(M)]
    for i in range(M):
        a[i], b[i] = map(int, input().split())
    Q = int(input())
    s = [None for _ in range(Q)]
    t = [None for _ in range(Q)]
    for i in range(Q):
        s[i], t[i] = map(int, input().split())
    n, a1 = solve(N, M, a, b, Q, s, t)
    print(n)
    for i in range(n):
        print(a1[i])


if __name__ == '__main__':
    main()
