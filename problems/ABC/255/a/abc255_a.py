#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[int]) -> int:
def solve(R, C, A):
    return A[R-1][C-1]

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    # failed to analyze input format
    R, C = map(int, input().split())
    A = list(list(map(int, input().split())) for _ in range(2))
    a = solve(R, C, A)
    print(a)


if __name__ == '__main__':
    main()
