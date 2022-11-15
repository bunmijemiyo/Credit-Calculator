# put your python code here
aa = []
sq_box = []
while True:
    n = int(input())
    aa.append(n)
    if sum(aa) == 0:
        break
    else:
        continue
for num in aa:
    sq_box.append(num**2)
print(sum(sq_box))