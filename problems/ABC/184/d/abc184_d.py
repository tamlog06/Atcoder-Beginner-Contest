#!/usr/bin/env python3
# from typing import *


# def solve(A: int, B: int, C: int) -> float:
def solve(A, B, C):
    k = 0
    N = A + B + C
    while max(A, B, C) < 100:
        A += 2*A/N
        B += 2*B/N
        C += 2*C/N
        k += 1
        N += 2*(A+B+C)/N

    return k

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A, B, C = map(int, input().split())
    a = solve(A, B, C)
    print(a)


if __name__ == '__main__':
    main()
