#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)


# def solve(n: int, a: List[int]) -> Tuple[int, int, int, int]:
def solve(n, a):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    # failed to analyze input format
    n = int(input())  # TODO: edit here
    a = list(map(int, input().split()))  # TODO: edit here
    a, b, c, d = solve(n, a)
    print(a)
    print(b)
    print(c)
    print(d)


if __name__ == '__main__':
    main()