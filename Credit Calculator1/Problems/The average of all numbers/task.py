# put your python code here
a = int(input())
b = int(input())
total = 0
counter = 0
for n in range(a, (b + 1)):
    if n % 3 == 0:
        total += n
        counter += 1
print(total / counter)