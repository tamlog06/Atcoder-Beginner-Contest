#!/usr/bin/env python3
# from typing import *


# def solve(W: int, H: int, N: int, x: List[int], y: List[int], a: List[int]) -> int:
def solve(W, H, N, x, y, a):
    coordinates = [[0, 0], [W, H]]
    for i in range(N):
        if a[i] == 1:
            coordinates[0][0] = max(coordinates[0][0], x[i])
        elif a[i] == 2:
            coordinates[1][0] = min(coordinates[1][0], x[i])
        elif a[i] == 3:
            coordinates[0][1] = max(coordinates[0][1], y[i])
        else:
            coordinates[1][1] = min(coordinates[1][1], y[i])
    
    if coordinates[1][0] <= coordinates[0][0] or coordinates[1][1] <= coordinates[0][1]:
        return 0
    else:
        return max(0, (coordinates[1][0] - coordinates[0][0]) * (coordinates[1][1] - coordinates[0][1]))


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    W, H, N = map(int, input().split())
    x = [None for _ in range(N)]
    y = [None for _ in range(N)]
    a = [None for _ in range(N)]
    for i in range(N):
        x[i], y[i], a[i] = map(int, input().split())
    a1 = solve(W, H, N, x, y, a)
    print(a1)


if __name__ == '__main__':
    main()
