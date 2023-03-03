#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache


# def solve(N: int) -> Any:
def solve(N):
    indexes = []
    for i in range(N.bit_length()):
        if N & (1 << i):
            indexes.append(i)

    for i in range(1<<len(indexes)):
        tmp = 0
        for j in range(len(indexes)):
            if i & (1 << j):
                tmp += 1 << indexes[j]
        print(tmp)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    solve(N)


if __name__ == '__main__':
    main()
