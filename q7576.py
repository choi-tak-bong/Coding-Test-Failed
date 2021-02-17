"""
https://www.acmicpc.net/problem/7576

◈ 실패 사유 : 메모리 초과
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

tomato_coords = []
new_tomato_coords = []

is_decay_all = True

day = 0

def decay_tomato(x, y):
    # 좌표값이 한계치를 벗어나면 함수 종료
    if x < 0 or y < 0 or x > len(board[0]) - 1 or y > len(board) - 1:
        return
    # 토마토를 익게 한다.
    if board[y][x] == -9999:
        board[y][x] = 1
        new_tomato_coords.append([x, y])

def test_tomato(x, y):
    # 좌표값이 한계치를 벗어나면 함수 종료
    if x < 0 or y < 0 or x > len(board[0]) - 1 or y > len(board) - 1:
        return
    # 이미 익은 곳이거나 울타리인 경우 함수 종료
    if board[y][x] == -9999 or board[y][x] == -1:
        return
    # 토마토 익히기
    board[y][x] = -9999
    # 상하좌우로 익히기
    test_tomato(x, y - 1)
    test_tomato(x, y + 1)
    test_tomato(x - 1, y)
    test_tomato(x + 1, y)

# 토마토들의 좌표를 입력한다.
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            tomato_coords.append([j, i])

# 토마토가 다 익는지 안 익는지 확인한다.
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            test_tomato(j, i)

for line in board:
    if 0 in line:
        is_decay_all = False

# 토마토가 전부 익지 못할 경우
if not is_decay_all:
    print(-1)
else:
    for coord in tomato_coords:
        board[coord[1]][coord[0]] = 1
    is_all = False
    while True:
        # 다 익었는지 확인한다.
        for line in board:
            if -9999 in line:
                is_all = False
                break
            else:
                is_all = True
        if is_all:
            break
        for tomato_coord in tomato_coords:
            decay_tomato(tomato_coord[0], tomato_coord[1] - 1) # 상
            decay_tomato(tomato_coord[0], tomato_coord[1] + 1) # 하
            decay_tomato(tomato_coord[0] - 1, tomato_coord[1]) # 좌
            decay_tomato(tomato_coord[0] + 1, tomato_coord[1]) # 우
        tomato_coords = [list(c) for c in new_tomato_coords]
        new_tomato_coords = []
        day += 1
    
    print(day)

