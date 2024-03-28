user_word = input("")

result_word = ''
for i in range(0, len(user_word)):
    if user_word[i] == "=":
        result_word = result_word[:-1]
    else:
        result_word += user_word[i]

print(result_word)
