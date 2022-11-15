category = int(input())
if category < 1:
    print("no army")
elif 1 <= category <= 9:
    print("few")
elif 10 <= category <= 49:
    print("pack")
elif 50 <= category <= 499:
    print("horde")
elif 500 <= category <= 999:
    print("swarm")
elif category >= 999:
    print("legion")
