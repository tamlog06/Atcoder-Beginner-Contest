#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, U: List[int], V: List[int]) -> int:
def solve(N, M, U, V):
    edges = [[False] * N for _ in range(N)]

    for u, v in zip(U, V):
        edges[u - 1][v - 1] = True
        edges[v - 1][u - 1] = True

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if edges[i][j] and edges[j][k] and edges[k][i]:
                    ans += 1

    return ans



# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    U = [None for _ in range(M)]
    V = [None for _ in range(M)]
    for i in range(M):
        U[i], V[i] = map(int, input().split())
    a = solve(N, M, U, V)
    print(a)


if __name__ == '__main__':
    main()
