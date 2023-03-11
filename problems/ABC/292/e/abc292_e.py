#!/usr/bin/env python3
import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache

import platform
if platform.python_implementation() == 'PyPy':
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    edges = [set() for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        edges[u-1].add(v-1)


    ans = set()
    for i in range(N):
        que = deque(edges[i])

        visited = set()
        visited.add(i)

        while que:
            j = que.popleft()
            if j in visited:
                continue

            visited.add(j)

            for k in edges[j]:
                if k in visited or k in edges[i]:
                    continue

                que.append(k)
                # edges[i].add(k)
                # ans += 1
                ans.add((i, k))

    print(len(ans))

main()