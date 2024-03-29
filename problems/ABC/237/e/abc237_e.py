#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)


# def solve(N: int, M: int, H: List[int], U: List[int], V: List[int]) -> int:
def solve(N, M, H, U, V):
    edges = [[] for _ in range(N)]

    for i in range(M):
        u = U[i] - 1
        v = V[i] - 1

        # H[u] <= H[v]にする
        if H[u] > H[v]:
            u, v = v, u

        edges[v].append([u, -(H[v] - H[u])])
        edges[u].append([v, 2*(H[v] - H[u])])

    d = [float('inf') for _ in range(N)]
    d[0] = 0

    for _ in range(N):
        update = False
        for i in range(N):
            for j, c in edges[i]:
                if d[i] + c < d[j]:
                    d[j] = d[i] + c
                    update = True

        if not update:
            break

    return -min(d)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    H = [None for _ in range(N)]
    U = [None for _ in range(M)]
    V = [None for _ in range(M)]
    for i in range(N):
        H[i] = int(next(tokens))
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, H, U, V)
    print(a)


if __name__ == '__main__':
    main()
