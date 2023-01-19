#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[int]) -> Any:
def solve(H, W, D, A, Q, LR):
    coordinates = [None for _ in range(H*W+1)]
    for i in range(H):
        for j in range(W):
            coordinates[A[i][j]] = (i, j)

    # print(coordinates)
    costs = [[0] for _ in range(D)]
    costs[0].append(0)

    for i in range(1, D+1):
        for j in range(i+D, H*W+1, D):
            # print(coordinates[j], coordinates[j-D])
            cost = abs(coordinates[j][0] - coordinates[j-D][0]) + abs(coordinates[j][1] - coordinates[j-D][1])
            costs[i%D].append(costs[i%D][-1] + cost)

    # print(costs)
    for l, r in LR:
        print(costs[l%D][r//D] - costs[l%D][l//D])
            

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    H, W, D = map(int, input().split())
    A = list(list(map(int, input().split())) for _ in range(H))
    Q = int(input())
    LR = list(list(map(int, input().split())) for _ in range(Q))

    solve(H, W, D, A, Q, LR)

if __name__ == '__main__':
    main()
