student_score = float(input())
max_score = float(input())
percentage_score = (student_score / max_score) * 100
if 90 <= percentage_score <= 100:
    print("A")
elif 80 <= percentage_score < 90:
    print("B")
elif 70 <= percentage_score < 80:
    print("C")
elif 60 <= percentage_score < 70:
    print("D")
elif percentage_score < 60:
    print("F")