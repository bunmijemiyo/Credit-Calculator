n = int(input())
if n <= 1:
    print("This number is not prime")
else:
    for m in range(2, n):
        if n % m == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")