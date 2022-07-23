#!/usr/bin/env python3
# from typing import *


# def solve(N: int, K: int, P: List[int]) -> List[str]:
def solve(N, K, P):
    ans = [-1]*N
    up = []
    for i in range(N):
        tmp = -1
        for j in range(len(up)):
            if up[j][-1] >= P[i]:
                if tmp == -1 or up[j][-1] < up[tmp][-1]:
                    tmp = j

        # print(tmp)
        if tmp != -1:
            up[tmp].append(P[i])
        else:
            up.append([P[i]])
        # print(up)
        if len(up[tmp]) == K:
            for j in up[tmp]:
                ans[j-1] = i+1
            up.pop(tmp)
    return ans

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    K = int(next(tokens))
    P = [None for _ in range(N)]
    for i in range(N):
        P[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, K, P)
    for i in range(N):
        print(ans[i])


if __name__ == '__main__':
    main()