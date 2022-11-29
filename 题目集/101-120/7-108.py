from sys import stdin
str_input = stdin.read()
text = str_input[:str_input.find("%%%")].lower()
for element in text:
    if element.isdigit() or element in "!.,:*?#":
        text = text.replace(element, " ")
word_dict = {}
for word in text.split():
    word_dict[word] = word_dict.get(word, 0) + 1
out_list = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
print(len(word_dict))
for out in out_list[:6]:
    print(*out, sep="=")