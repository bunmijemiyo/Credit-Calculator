x = float(input())
y = float(input())
if x >= 0.0 and y >= 0.0:
    print("I")
elif x >= 0.0 and y <= 0.0:
    print("IV")
elif x <= 0.0 and y >= 0.0:
    print("II")
elif x <= 0.0 and y <= 0.0:
    print("III")