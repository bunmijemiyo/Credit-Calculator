name_list = []

while True:
    name = input()
    if name != ".":
        name_list.append(name)
    else:
        break
print(name_list)
print(len(name_list))