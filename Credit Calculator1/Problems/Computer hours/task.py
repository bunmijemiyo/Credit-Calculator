# Make sure your output matches the assignment *exactly*
computer_hrs = int(input())
if computer_hrs < 2:
    print("That seems reasonable")
elif computer_hrs < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")