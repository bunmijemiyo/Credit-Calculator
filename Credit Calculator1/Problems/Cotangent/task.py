import math
angle_ = float(input())
angle = math.radians(angle_)
cotangent = math.cos(angle) / math.sin(angle)
print(round(cotangent, 10))