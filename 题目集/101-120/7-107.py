from sys import stdin
str_input = stdin.read()
text = str_input[:str_input.find("!!!!!")].lower()
for element in text:
    if element in "!.,:*?":
        text = text.replace(element, " ")
word_list = text.lower().split()
word_dict = {}
for word in word_list:
    word_dict[word] = word_dict.get(word, 0) + 1
print(len(word_dict))
out_list = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
for out in out_list[:10]:
    print(*out, sep='=')
