#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(N: int) -> str:
def solve(N):
    N = list(str(N))

    if '7' in N:
        return YES
    else:
        return NO


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
