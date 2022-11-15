amount = int(input())
if amount < 23:
    print("None")
elif amount < 678:
    chick_num = amount // 23
    if chick_num > 1:
        print(chick_num, "chickens")
    else:
        print(chick_num, "chicken")
elif amount < 1296:
    goat_num = amount // 678
    if goat_num > 1:
        print(goat_num, "goats")
    else:
        print(goat_num, "goat")
elif amount < 3848:
    pig_num = amount // 1296
    if pig_num > 1:
        print(pig_num, "pigs")
    else:
        print(pig_num, "pig")
elif amount < 6769:
    cow_num = amount // 3848
    if cow_num > 1:
        print(cow_num, "cows")
    else:
        print(cow_num, "cow")
elif amount >= 6769:
    sheep_num = amount // 6769
    print(sheep_num, "sheep")