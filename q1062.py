n, k = map(int, input().split())
south_words = [list(set(input()[4:-4])) for _ in range(n)]
south_words.sort(key=lambda x: len(x))

educated_char_number = 0
educated_word_number = 0
educated_char_table = [False] * (ord("z") - ord("a") + 1)

south_lang = list(set("antatica"))

# 남극어 먼저 학습
for i in range(len(south_lang)):
    char_index = ord(south_lang[i]) - ord("a")
    if not educated_char_table[char_index]:
        educated_char_table[char_index] = True
        educated_char_number += 1

for word in south_words: # 모든 단어들을 탐색한다.
    for i in range(len(word)): # 단어들의 글자들을 검토한다.
        char_index = ord(word[i]) - ord("a")
        if i == len(word) - 1 and educated_char_number:
            pass

print(educated_word_number)
