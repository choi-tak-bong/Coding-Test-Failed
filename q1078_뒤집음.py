from sys import stdin

input = stdin.readline

def one_one_one(count: int):
    result = ""
    for _ in range(count):
        result += "1"
    return int(result)

def number_len(number: int):
    i = 1

    while True:
        if 9 * one_one_one(i) <= number < 9 * one_one_one(i+1):
            break
        i += 1

    return i

def solution():
    d = int(input())

    if d == 0:
        return 1
    else:
        one_one = one_one_one(number_len(d))
        leng_d = number_len(d)
        answer = 0
        div, mod = divmod(d, 9 * one_one) # D를 111...*n으로 나눈 몫과 나머지
        print(div, mod)

        if div != 10 and mod == 0: # 몫이 10이 아니여야 하며, 나머지가 0이여야 한다.
            answer = div * 10 ** leng_d
            return answer
        elif div == 10 and mod == 0:
            temp = "11"
            for _ in range(leng_d):
                temp += "0"
            temp += "1"
            return int(temp)
        else:
            return -1

print(solution())