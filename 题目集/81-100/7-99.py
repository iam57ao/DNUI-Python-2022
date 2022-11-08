value = input().split()
ready = "I'm ready!"
print("Teacher: Hi everyone, are you ready?")
for element in value:
    print_list = []
    for i in range(value.index(element) + 1):
        print_list.append(ready)
    print(f"{element}: ", end='')
    print(*print_list)
print("Teacher: OK! Let's start our exam.")
