#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
from functools import lru_cache

# def solve(Q: int, A: int, B: int, t: List[int], a: List[int], b: List[int]) -> Any:
def solve(Q, A, B, t, a, b):
    return 


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    Q, A, B = map(int, input().split())
    t = [None for _ in range(Q)]
    a = [None for _ in range(Q)]
    b = [None for _ in range(Q)]
    for i in range(Q):
        t[i], a[i], b[i] = map(int, input().split())
    ans = solve(Q, A, B, t, a, b)
    print(ans)  # TODO: edit here

if __name__ == '__main__':
    main()
