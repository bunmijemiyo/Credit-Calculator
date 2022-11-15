# This program takes inputs and find its mean
num_list = []
total = 0
while True:
    n = input()
    if n != ".":
        num_list.append(n)
    else:
        break
for num in num_list:
    total += int(num)
mean = total / len(num_list)
print(mean)