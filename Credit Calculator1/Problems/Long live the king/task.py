# A program to check the count of king movement on a chess board
y_column = int(input())
x_row = int(input())
if y_column in [1, 8]:
    if x_row in [1, 8]:
        print("3")
    elif x_row in range(2, 8):
        print("5")
elif y_column in range(2, 8) and x_row in range(2, 8):
    print("8")
elif y_column in range(2, 8):
    if x_row in [1, 8]:
        print("5")