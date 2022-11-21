from sys import stdin
str_input = stdin.read()
text = str_input[:str_input.find("#")]
for element in text:
    if not element.isalnum() and element != "_":
        text = text.replace(element, " ")
word_dict = {}
for word in text.lower().split():
    word = word[:15]
    word_dict[word] = word_dict.get(word, 0) + 1
word_list = sorted(word_dict.items(), key=lambda word_count: (-word_count[1], word_count[0]))
print(len(word_list))
for out in range(len(word_dict) // 10):
    print(f"{word_list[out][1]}:{word_list[out][0]}")