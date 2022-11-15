import math
n = int(input())
for _ in range(n):
    number = int(input())
    if number % 7 == 0:
        print(int(math.pow(number, 2)))