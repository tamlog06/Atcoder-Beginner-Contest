#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, v: int, A: List[int], B: List[int], C: List[int]) -> str:
def solve(N, M, v, A, B, C):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, v = map(int, input().split())
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    C = [None for _ in range(M)]
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    a = solve(N, M, v, A, B, C)
    print(a)


if __name__ == '__main__':
    main()
