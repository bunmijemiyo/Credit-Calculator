import math
num = abs(int(input()))
base = int(input())
if base > 1:
    num_log = math.log(num, base)
    print(round(num_log, 2))
else:
    num_log = math.log(num)
    print(round(num_log, 2))