import math
x = int(input())
sigmoid = 1 / (1 + math.exp(-x))
print(round(sigmoid, 2))