#!/usr/bin/env python3
# from typing import *


# def solve(A: int, B: int, C: int, K: int) -> int:
def solve(A, B, C, K):
    if K <= A+B:
        return min(K, A)
    else:
        return A - (K - A - B)

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A, B, C, K = map(int, input().split())
    a = solve(A, B, C, K)
    print(a)


if __name__ == '__main__':
    main()
