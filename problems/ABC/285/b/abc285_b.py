#!/usr/bin/env python3
# from typing import *


# def solve(N: int, S: str) -> List[str]:
def solve(N, S):
    S = ' '+S
    ans = []
    for i in range(1, N):
        ans.append(0)
        for k in range(1, N-i+1):
            if S[k] != S[k+i]:
                ans[-1] += 1
            else:
                break
    return ans

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    S = input()
    a = solve(N, S)
    for i in range(N-1):
        print(a[i])


if __name__ == '__main__':
    main()
