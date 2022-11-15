# put your python code here
first_number = float(input())
second_number = float(input())
arith_opera = input()
if second_number == 0.0 and arith_opera in ["mod", "/", "div"]:
    print("Division by 0!")
else:
    if arith_opera == "mod":
        print(first_number % second_number)
    elif arith_opera == "div":
        print(first_number // second_number)
    elif arith_opera == "/":
        print(first_number / second_number)
    elif arith_opera == "*":
        print(first_number * second_number)
    elif arith_opera == "pow":
        print(first_number ** second_number)
    elif arith_opera == "+":
        print(first_number + second_number)
    elif arith_opera == "-":
        print(first_number - second_number)