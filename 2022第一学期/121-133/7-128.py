def longWord(input_str):
    for element in input_str:
        if not element.isalnum():
            input_str = input_str.replace(element, " ")
    word_list = input_str.split()
    longest_index = 0
    for word in word_list:
        if len(word) > len(word_list[longest_index]):
            longest_index = word_list.index(word)
    return word_list[longest_index]


while True:
    try:
        print(longWord(input()))
    except EOFError:
        break
