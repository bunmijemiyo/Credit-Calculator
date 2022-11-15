import math
edge_length = int(input())
areaa = 2 * math.sqrt(3) * math.pow(edge_length, 2)
area = round(areaa, 2)
vol = (1 / 3) * math.sqrt(2) * math.pow(edge_length, 3)
volume = round(vol, 2)
print(f"{area} {volume}")
