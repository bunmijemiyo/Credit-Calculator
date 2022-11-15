# a program to check for minimum value for an inputted list
float_list = []
while True:
    float_input = input()
    if float_input == ".":
        break
    else:
        float_list.append(float(float_input))
print(min(float_list))