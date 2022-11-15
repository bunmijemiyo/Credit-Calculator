scores = input().split()
# put your python code here
correct_ans = 0
incorrect_ans = 0
if 15 <= len(scores) < 50:
    for word in scores:
        incorrect_ans += word.count("I")
        correct_ans += word.count("C")
        if incorrect_ans == 3:
            print("Game over")
            print(correct_ans)
            break

    else:
        print("You won")
        print(scores.count("C"))
else:
    pass