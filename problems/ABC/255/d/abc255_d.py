#!/usr/bin/env python3
# from typing import *

MOD = 998244353


# def solve(N: int, Q: int, A: List[int], X: List[int]) -> List[str]:
def solve(N, Q, A, X):
    A.sort()
    ans = [0 for _ in range(Q)]
    Cum_sum = [0 for _ in range(N + 1)]
    for i in range(N):
        Cum_sum[i + 1] = Cum_sum[i] + A[i]

    for i in range(Q):
        left = 0
        right = N-1
        print(A, X[i])
        while True:
            mid = (left + right) // 2
            print(left, right, mid)
            input()

            if right == left:
                if right == 0:
                    k = 0
                    break
                elif right == N-1:
                    k = N-1
                    break
            elif A[mid] <= X[i] <= A[mid+1]:
                k = mid
                break

            if X[i] < A[mid]:
                right = mid - 1
            else:
                left = mid + 1

        ans[i] = k*X[i] - Cum_sum[k] - (N-k)*X[i] + (Cum_sum[N] - Cum_sum[k])

    return ans

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = list(int(input()) for _ in range(Q))
    a = solve(N, Q, A, X)
    for i in range(Q):
        print(a[i])


if __name__ == '__main__':
    main()
