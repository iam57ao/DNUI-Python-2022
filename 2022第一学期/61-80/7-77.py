str_input = input()
str_output = ""
for element in str_input:
    if element.islower():
        str_output += chr(122 - ord(element) + 97)
    elif element.isupper():
        str_output += chr(90 - ord(element) + 65)
    else:
        str_output += element
print(str_output)
