synthesis_index = float(input())
if synthesis_index > 3:
    print("Polysynthetic")
elif 2 <= synthesis_index <= 3:
    print("Synthetic")
elif synthesis_index < 2:
    print("Analytic")