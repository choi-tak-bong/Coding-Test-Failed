from sys import stdin

input = stdin.readline

n = int(input())
prices = list(map(int, input().split()))
m = int(input())

min_value = min(prices)
min_index = n - 1

for i in range(n - 1, -1, -1):
    if prices[min_index] > prices[i]:
        min_index = i

cur_m = m - (min_value * ((m // min_value) if m // min_value < 100 else 100))
dp = [min_index] * ((m // min_value) if m // min_value < 100 else 100)

start_pointer = 0
pointer_move = True

for i in range(len(dp)):
    cur_m += min_value # 기존에 배치된 번호를 되팔아서 기존에 배치된 번호의 가격 만큼 확보한다.

    for j in range(n - 1, -1, -1):
        if prices[j] <= cur_m and j > 0: # 번호를 살 수 있는 경우, 가격이 번호 0의 가격보다 비싼 경우
            cur_m -= prices[j]
            dp[i] = j
            pointer_move = False
            break
        elif prices[j] <= cur_m and j == 0 and pointer_move:
            start_pointer += 1
        elif prices[j] <= cur_m and j == 0 and not pointer_move:
            cur_m -= prices[j]

dp = dp[start_pointer:]

print(len(dp) if m < 100 else m)

if len(dp) <= 50:
    print("".join(map(str, dp)) if start_pointer < len(dp) else 0)
    print("".join(map(str, dp)) if start_pointer < len(dp) else 0)
else:
    print("".join(map(str, dp[:50])))
    print("".join(map(str, dp[-50:])))

