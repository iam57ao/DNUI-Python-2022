from sys import stdin
input_str = stdin.read()
text = input_str[:input_str.find("!!!!!")]
word_dict = {}
for word in text.split():
    word_dict[word] = word_dict.get(word, 0) + 1
print(len(word_dict))
for out in sorted(word_dict.keys())[:10]:
    print(out)