thislist = ["apple", "banana", "cherry"]
thislist[1] = "balckcurrant"
print(thislist)

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:3] = ["blackcurrant", "watermelon"]
print(thislist1)

thislist2 = ["apple", "banana", "cherry"]
thislist2[1:2] = ["blackcurrant", "watermelon"]
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
thislist3[1:3] = ["watermelon"]
print(thislist3)

thislist4 = ["apple", "banana", "cherry"]
thislist4.insert(2, "watermelon")
print(thislist4)