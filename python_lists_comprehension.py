# приклад без list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
# приклад list comprehension
newlist1 = [x for x in fruits if "a" in x]
print(newlist1)

# Синтаксис розуміння списку (list comprehension)
# newlist = [expression for item in iterable if condition == True]
newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)
# без умови
newlist3 = [x for x in fruits]
print(newlist3)
# ітерований список
newlist4 = [x for x in range(10)]
print(newlist4)

newlist5 = [x for x in range(10) if x < 5]
print(newlist5)

# expresion, маніпулювання виразом до того, як він стане частиною нового списку
newlist6 = [x.upper() for x in fruits]
print(newlist6)

newlist7 = ["hello" for x in fruits]
print(newlist7)

# вираз не як фільтр, а як спосіб маніпулювати результатом
newlist8 = [x if x != "banana" else "orange" for x in fruits]
print(newlist8)
