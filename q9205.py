from typing import List

t = int(input())
answers = []

def compute_way_to_festival(move_routes: List[List[int]]):
    x, y = move_routes[0]
    state = "happy"
    for move_route in move_routes[1:]:
        if (abs(x - move_route[0]) + abs(y - move_route[1])) <= 1000:
            x = move_route[0]
            y = move_route[1]
        else:
            state = "sad"
            answers.append(state)
            return
    answers.append(state)

for i in range(t):
    n = int(input())
    home_coord = list(map(int, input().split()))
    conv_coords = [list(map(int, input().split())) for _ in range(n)]
    fest_coord = list(map(int, input().split()))
    move_routes = [home_coord] + conv_coords + [fest_coord]
    compute_way_to_festival(move_routes)

for state in answers:
    print(state)