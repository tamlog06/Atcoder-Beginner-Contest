#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: int, Y: int) -> int:
def solve(N, X, Y):
    A = 1
    B = 0
    if N == 1:
        return 0
    for i in range(N-1):
        B += A*X
        A += B
        B *= Y

    return B


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, X, Y = map(int, input().split())
    a = solve(N, X, Y)
    print(a)


if __name__ == '__main__':
    main()