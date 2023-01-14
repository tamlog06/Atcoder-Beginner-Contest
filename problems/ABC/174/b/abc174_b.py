#!/usr/bin/env python3
# from typing import *


# def solve(N: int, D: int, X: List[int], Y: List[int]) -> int:
def solve(N, D, X, Y):
    ans = 0
    for i in range(N):
        if X[i] ** 2 + Y[i] ** 2 <= D ** 2:
            ans += 1
    return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, D = map(int, input().split())
    X = [None for _ in range(N)]
    Y = [None for _ in range(N)]
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    a = solve(N, D, X, Y)
    print(a)


if __name__ == '__main__':
    main()
