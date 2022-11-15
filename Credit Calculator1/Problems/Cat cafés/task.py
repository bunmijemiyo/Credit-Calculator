cat_list = []
cat_names = []
while True:
    cafe_cats = input()
    if cafe_cats == "MEOW":
        break
    else:
        dew = cafe_cats.split()
        num = int(dew[1])
        name = dew[0]
        cat_list.append(num)
        cat_names.append(name)
# taking kk as the maximum number of cats
# since lists are ordered, I added name and num into separate list
# i got the index of the maximum number, then use the index to get the cat name
# the logic here is that both will have the same index
kk = max(cat_list)
ss = cat_list.index(kk)
print(cat_names[ss])