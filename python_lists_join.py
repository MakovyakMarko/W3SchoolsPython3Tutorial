list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# ще один спосіб додати списки, це приєднати до першого другий по одному елементу
for x in list2:
    list1.append(x)
print(list1)
# або можна скористатись методом extend()
list11 = ["a", "b", "c"]
list12 = [1, 2, 3]

list11.extend(list12)
print(list11)
