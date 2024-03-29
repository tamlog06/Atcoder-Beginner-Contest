#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, K: int, u: List[int], v: List[int], a: List[int], s: List[int]) -> int:
# def solve(N, M, K, u, v, a, s):
    # edges = []
    # for i in range(M):
        # edges.append((u[i], v[i], a[i]))

    # d_0 = [float('inf')] * (N + 1)
    # d_1 = [float('inf')] * (N + 1)
    # d_0[1] = 0

    # S = [-1] * (N + 1)
    # for i in range(K):
        # S[s[i]] = 1

    # for i in range(2*N):
        # updated = False

        # for j in range(M):
            # u, v, a = edges[j]
            # if a == 0:
                # if d_1[u] != float('inf') and d_1[v] > d_1[u] + 1:
                    # d_1[v] = d_1[u] + 1
                    # updated = True

                # if d_1[v] != float('inf') and d_1[u] > d_1[v] + 1:
                    # d_1[u] = d_1[v] + 1
                    # updated = True

            # if a == 1:
                # if d_0[u] != float('inf') and d_0[v] > d_0[u] + 1:
                    # d_0[v] = d_0[u] + 1
                    # updated = True

                # if d_0[v] != float('inf') and d_0[u] > d_0[v] + 1:
                    # d_0[u] = d_0[v] + 1
                    # updated = True

            # if S[u] == 1 and (d_0[u] != float('inf') or d_1[u] != float('inf')):
                # d = min(d_0[u], d_1[u])
                # d_0[u] = d
                # d_1[u] = d
                # updated = True

            # if S[v] == 1 and (d_0[v] != float('inf') or d_1[v] != float('inf')):
                # d = min(d_0[v], d_1[v])
                # d_0[v] = d
                # d_1[v] = d
                # updated = True

        # if not updated:
            # break

    # if d_0[N] == float('inf') and d_1[N] == float('inf'):
        # return -1
    # else:
        # return min(d_0[N], d_1[N])

import heapq
def solve(N, M, K, u, v, a, s):
    cost = [{} for _ in range(2*N + 1)]

    for i in range(M):
        if a[i] == 1:
            cost[u[i]][v[i]] = 1
            cost[v[i]][u[i]] = 1
        else:
            cost[u[i]+N][v[i]+N] = 1
            cost[v[i]+N][u[i]+N] = 1

    for i in range(K):
        cost[s[i]][s[i]+N] = 0
        cost[s[i]+N][s[i]] = 0

    d = [float('inf')] * (2*N + 1)
    d[1] = 0
    q = [(0, 1)]

    while q:
        distance, node = heapq.heappop(q)
        if d[node] < distance:
            continue

        if node == N or node == 2*N:
            break

        for next_node, next_cost in cost[node].items():
            if d[next_node] > d[node] + next_cost:
                d[next_node] = d[node] + next_cost
                heapq.heappush(q, (d[next_node], next_node))

    if d[N] == float('inf') and d[2*N] == float('inf'):
        return -1
    else:
        return min(d[N], d[2*N])
        

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    K = int(next(tokens))
    u = [None for _ in range(M)]
    v = [None for _ in range(M)]
    a = [None for _ in range(M)]
    s = [None for _ in range(K)]
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        a[i] = int(next(tokens))
    for i in range(K):
        s[i] = int(next(tokens))
    assert next(tokens, None) is None
    a1 = solve(N, M, K, u, v, a, s)
    print(a1)


if __name__ == '__main__':
    main()
