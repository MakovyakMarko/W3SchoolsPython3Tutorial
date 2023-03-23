thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)

thislist1 = ["apple", "banana", "cherry"]
print(thislist1)
thislist1.pop(0)
print(thislist1)

thislist2 = ["apple", "banana", "cherry"]
print(thislist2)
thislist2.pop()
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
print(thislist3)
del thislist3[1]
print(thislist3)

thislist4 = ["apple", "banana", "cherry"]
print(thislist4)
del thislist4
# print error "name 'thislist4' is not defined

thislist5 = ["apple", "banana", "cherry"]
thislist5.clear()
print(thislist5)