thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print("Не сортований: ", thislist)
thislist.sort()
print("Посортований: ", thislist)
thislist1 = [100, 98, 2, 35, 101]
print("Не сортований: ", thislist1)
thislist1.sort()
print("Посортований: ", thislist1)

thislist.sort(reverse=True)
print("Посортований в зворотньому порядку", thislist)
thislist1.sort(reverse=True)
print("Посортований в зворотньому порядку", thislist1)

# відсортуйте список в залежності від того, наскільки близьке число до 50 (key = function)
def myfunc(n):
    return abs(n - 50)
thislist2 = [100, 50, 65, 82, 23]
thislist2.sort(key = myfunc)
print("Найближче до 50: ", thislist2)

# sort() чутливий до регістру, великі букви сортуються перед малими
# сортування з урахуванням регістру може дати неочікуваний результат
thislist3 = ["banana", "Orange", "Kiwi", "cherry"]
thislist3.sort()
print("Сортує з урахуванням регістру: ", thislist3)
# приклад сортування без урахування регістру - str.lower
thislist3.sort(key = str.lower)
print("Сортує без урахування регітсру: ", thislist3)
# змініть порядок елементів списку на протилежний
thislist3.reverse()
print("Змінює порядок на протилежний: ", thislist3)