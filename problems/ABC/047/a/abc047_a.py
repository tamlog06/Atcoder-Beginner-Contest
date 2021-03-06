#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(a: int, b: int, c: int) -> str:
def solve(a, b, c):
    candy = [a, b, c]
    candy.sort()
    if sum(candy[:2]) == candy[2]:
        return YES
    else:
        return NO

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    a, b, c = map(int, input().split())
    a1 = solve(a, b, c)
    print(a1)


if __name__ == '__main__':
    main()
