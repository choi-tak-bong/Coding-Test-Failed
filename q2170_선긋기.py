"""
https://www.acmicpc.net/problem/1946

◈실패 사유: 시간 초과, 틀렸습니다.
"""

import sys

input = sys.stdin.readline

n = int(input())
lines = sorted([list(map(int, input().split())) for _ in range(n)])

answer = 0

min_value = 1e9
max_value = 0

for i in range(len(lines) - 1):
    now_line = lines[i]
    next_line = lines[i+1]
    min_value = min_value if min_value < now_line[0] else now_line[0]
    max_value = max_value if max_value > now_line[1] else now_line[1]
    
    if max_value < next_line[0]:
        answer += max_value - min_value
        min_value = next_line[0]
        max_value = next_line[1]

answer += max_value - min_value

print(answer)
