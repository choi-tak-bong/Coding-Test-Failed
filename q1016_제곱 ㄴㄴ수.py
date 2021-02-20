"""
https://www.acmicpc.net/problem/q1016
"""

from sys import stdin

input = stdin.readline

min_val, max_val = map(int, input().split())

array = [True] * (max_val - min_val + 1)
answer = 0

n = 1

while n ** 2 <= max_val:
    n += 1
    k = n ** 2
    i = min_val // k

    while i * k <= max_val:
        j = k * i - min_val

        if j >= 0 and array[j]:
            answer += 1
            array[j] = False

print(max_val - min_val + 1 - answer)