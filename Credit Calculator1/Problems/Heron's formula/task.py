import math  # put your python code here
side_a = int(input())
side_b = int(input())
side_c = int(input())
p = (side_a + side_b + side_c) / 2
S = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
print(float(S))