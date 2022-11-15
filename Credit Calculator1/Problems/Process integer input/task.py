# put your python code here
ls = []

while True:
    n = int(input())
    if n < 10:
        continue
    elif 10 <= n <= 100:
        ls.append(n)
    elif n > 100:
        break
for num in ls:
    print(num)