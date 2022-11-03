a = input()
out = str()
for i in a:
    if i.isalpha and i.islower():
        i = ord(i)
        if i < 110:
            i += 2 * (110 - i) - 1
            out += chr(i)
        else:
            i -= 2 * (i - 109) - 1
            out += chr(i)
    elif i.isalpha and i.isupper():
        i = ord(i)
        if i < 78:
            i += 2 * (78 - i) - 1
            out += chr(i)
        else:
            i -= 2 * (i - 77) - 1
            out += chr(i)
    else:
        out += i
print(out)
